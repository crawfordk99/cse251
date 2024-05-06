import threading
import time
import random

VALUE = 10


def adder(amount: int, repeat_amount: int, lock: threading.Lock):
    global VALUE
    for _ in range(repeat_amount):
        with lock:
            # lock.acquire()
            tmp1 = VALUE
            time.sleep(random.uniform(0.001, 0.01))
            tmp1 += amount
            VALUE = tmp1
            # lock.release()


def subtractor(amount: int, repeat_amount: int, lock: threading.Lock):
    global VALUE
    for _ in range(repeat_amount):
        with lock:
            # lock.acquire()
            tmp2 = VALUE
            time.sleep(random.uniform(0.001, 0.01))
            tmp2 -= amount
            VALUE = tmp2
            # lock.release()


def main():

    repeat_amount = 100
    lock = threading.Lock()
    t1 = threading.Thread(target=adder, args=(1, repeat_amount, lock))
    t1.start()

    t2 = threading.Thread(target=subtractor, args=(1, repeat_amount, lock))
    t2.start()

    t1.join()
    t2.join()

    print(f'{VALUE=}')


if __name__ == "__main__":
    main()
