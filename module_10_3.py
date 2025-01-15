from threading import Lock, Thread
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self) -> None:
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            transaction = randint(50, 500)
            self.balance += transaction
            print(f"Пополнение: {transaction}. Баланс: {self.balance}")
        sleep(0.001)

    def take(self) -> None:
        for _ in range(100):
            transaction = randint(50, 500)
            print(f"Запрос на {transaction}")
            if transaction <= self.balance:
                self.balance -= transaction
                print(f"Снятие: {transaction}. Баланс: {self.balance}")
            else:
                self.lock.acquire()
                print('Запрос отклонён, недостаточно средств')


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
