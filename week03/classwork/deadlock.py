import threading
import time
import random


BALANCE = 0

def deposit(money: int, lock1: threading.Lock, lock2: threading.Lock):
    print(f'{threading.current_thread().name}: about to acquire lock1\n', end="")
    lock1.acquire()
    print(f'{threading.current_thread().name}: acquired lock1\n', end="")

    global BALANCE
    BALANCE += money
    
    time.sleep(0.1)
    print(f'{threading.current_thread().name}: about to acquire lock2\n', end="")
    lock2.acquire()
    print(f'{threading.current_thread().name}: acquired lock2\n', end="")
    
    lock1.release()
    lock2.release()


def main():

    lock1 = threading.Lock()
    lock2 = threading.Lock()
    
    t1 = threading.Thread(target=deposit, args=(100, lock1, lock2))
    t1.start()

    t2 = threading.Thread(target=deposit, args=(-50, lock2, lock1))
    t2.start()

    t1.join()
    t2.join()

    print(f'{BALANCE=}')


if __name__ == "__main__":
    main()