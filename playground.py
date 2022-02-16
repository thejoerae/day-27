def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(5, 4, 7, 9))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    # print(key)
    # print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        #self.make = kw["make"]
        # don't need to pass in argument with the get() method.
        # can be blank or added
        self.make = kw.get("make")
        #self.model = kw["model"]
        self.model = kw.get("model")


my_car = Car(make = "Nissan", model = "GT-8")
print(my_car)