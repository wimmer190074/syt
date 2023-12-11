import threading
import time
import random

global_lock = threading.Lock()

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        super().__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        for i in range(5):
            self.think()
            self.eat()

    def think(self):
        print(f"{self.name} is thinking.")
        time.sleep(random.uniform(1, 3))

    def eat(self):
        print(f"{self.name} is hungry and trying to pick up forks.")

        with global_lock:
            with self.left_fork:
                print(f"{self.name} picked up the left fork.")
                time.sleep(random.uniform(0.1, 1))

                with self.right_fork:
                    print(f"{self.name} picked up the right fork and is eating.")
                    time.sleep(random.uniform(1, 3))

        print(f"{self.name} finished eating and put down the forks.")

def main():
    num_philosophers = 5
    forks = [threading.Lock() for _ in range(num_philosophers)]
    philosophers = []

    for i in range(num_philosophers):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]
        philosopher = Philosopher(f"Philosopher {i + 1}", left_fork, right_fork)
        philosophers.append(philosopher)

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    main()