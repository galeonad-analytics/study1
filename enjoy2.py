# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from time import sleep
import multiprocessing as mp

def f(l1, l2):
    with l1:
        sleep(1)
    with l2:
        sleep(1)
    print('Наслаждайтесь бесконечностью...')


if __name__ == '__main__':
    l1 = mp.Lock()
    l2 = mp.Lock()
    p1 = mp.Process(target=f, args=(l1, l2))
    p2 = mp.Process(target=f, args=(l2, l1))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


