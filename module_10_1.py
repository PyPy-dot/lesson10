from time import sleep, perf_counter
import threading
from datetime import time


def write_words(word_count: int, file_name: str):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        print(f"Какое-то слово № {i}", file=file)
        sleep(0.1)
    else:
        print(f"Завершилась запись в файл {file_name}")
        file.close()


thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
t = perf_counter()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
print('Работа потоков ', time(second=int(perf_counter() - t), microsecond=int(perf_counter() - t * 100 % 100)))
t = perf_counter()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
threading.Thread(target=print, args=('Работа потоков ', time(second=int(perf_counter() - t),
                                                             microsecond=int(perf_counter() - t * 100 % 100)))).start()
