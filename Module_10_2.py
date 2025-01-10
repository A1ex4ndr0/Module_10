import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0

        while self.enemy:
            self.enemy -= self.power
            days += 1
            time.sleep(1)
            print(f"{self.name} сражается {days}..., осталось {self.enemy} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()