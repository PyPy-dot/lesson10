from datetime import datetime
from multiprocessing import Pool


def read_info(name: str) -> None:
    all_data = []
    with open(name, 'r') as file:
        for line in file.readlines():
            all_data.append(line.strip())


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

if __name__ == '__main__':
    start_time = datetime.now()
    for file_name in files:
        read_info(file_name)
    end_time = datetime.now()
    print(end_time - start_time, '(линейный)')

    start_time = datetime.now()
    with Pool() as p:
        p.map(read_info, files)
    end_time = datetime.now()
    print(end_time - start_time, '(многопроцессный)')