
import threading


def myFunction(a: int, b: int) -> int:
    #print(f'myFunction: a={id(a)}')
    #print(f'myFunction: b={id(b)}')
    a = 5
    b = 10
    #print(f'myFunction: AFTER a={id(a)}')
    #print(f'myFunction: AFTER b={id(b)}')
    
    return a

x = 1
y = 2

#print(f'BEFORE: {id(x)}')
#print(f'BEFORE: {id(y)}')

myFunction(x, y)

#print(f'AFTER: {id(x)}, {x=}')
#print(f'AFTER: {id(y)}, {y=}')

def myListFunction(l: list):
    #print(f'myFunction: l={id(l)}')
    l.append(20)
    #print(f'myFunction: AFTER l={id(l)}')

myList = []
#print(f'BEFORE: {id(myList)}')
myListFunction(myList)
#print(f'AFTER: {id(myList)}, {myList=}')

def myStringFunction(s: str):
    #print(f'myFunction: s={id(s)}')
    s = "new string"
    #print(f'myFunction: AFTER s={id(s)}')
    
my_string = "old string"
#print(f'BEFORE: {id(my_string)}')
myStringFunction(my_string)
#print(f'AFTER: {id(my_string)}, {my_string=}')

class ParentClass():
    def __init__(self, age: int, name: str, children_names: list):
        self.age = age
        self.name = name
        self.children_names = children_names
    
    def print_value(self):
        print(f'{self.age=}, {self.name=}, {self.children_names=}')
        

myClass = ParentClass(10, "Bob", ["A", "B", "C"])
myClass.print_value()

class ChildClass(ParentClass):
    def __init__(self, age: int, name: str, children_names: list, weight: int):
        super().__init__(age, name, children_names)
        self.weight = weight
    
    def print_value(self):
        super().print_value()
        print(f'{self.weight=}')
        
child = ChildClass(10, "name", ["A", "B", "C"], 490)
child.print_value()


# Creating a thread to compute the product of a range of numbers
t = threading.Thread(target=computerProduct, args=(number,))

# Start the computeProduct thread
t.start()

# Wait for the computerProduct thread to finish
t.join()