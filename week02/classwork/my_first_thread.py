
import threading
import time

def add_two_number(num1: int, num2: int, results: list, id: int):
    time.sleep(1.0)
    print(f'{threading.current_thread().name}: all done sleeping\n', end="")
    results[id] = num1 + num2

class SumThread(threading.Thread):
    def __init__(self, num1: int, num2: int, results: list, id: int):
        super().__init__()
        self.number1 = num1
        self.number2 = num2
        #self.result = 0
        self.results = results
        self.id = id
    
    def run(self):
        print(f'{threading.current_thread().name}: summing {self.number1} and {self.number2}\n', end="")
        time.sleep(0.5)
        #self.result = self.number1 + self.number2
        self.results[self.id] = self.number1 + self.number2

def main():
    
    using_thread_class_results = [int] * 10
    threads = []
    for i in range(10):
        t = SumThread(i, 200, using_thread_class_results, i)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
        #print(f'{t.result=}')
    
    print(f'{using_thread_class_results=}')
    
    
    #sum = add_two_number(3, 5)
    #print(f'{sum=}')
    """ results = [int] * 2
    
    t0 = threading.Thread(target=add_two_number, args=(3, 5, results, 0))
    t0.start()
    
    t1 = threading.Thread(target=add_two_number, args=(6, 7, results, 1))
    t1.start()
    
    t0.join()
    t1.join()
    
    print(f"{threading.current_thread().name}: {results=}") """
    
    
    

if __name__ == "__main__":
    main()
    print("All Done!")