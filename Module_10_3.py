import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        #self.balance = balance
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            rand = randint(50, 500)
            self.balance += rand
            print(f"Пополнение: {rand}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            rand = randint(50, 500)
            print(f"Запрос на {rand}")
            if rand <= self.balance:
                self.balance -= rand
                print(f"Снятие: {rand}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

