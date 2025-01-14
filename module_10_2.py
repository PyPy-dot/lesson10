from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int) -> None:
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy_count = 100
        self.day = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemy_count > 0:
            self.day += 1
            self.enemy_count -= self.power
            print(f'{self.name}, сражается {self.day} день(дня)..., осталось {self.enemy_count} воинов.')
            sleep(1)
        else:
            print(f"{self.name} одержал победу спустя {self.day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
