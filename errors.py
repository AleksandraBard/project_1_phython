# TYPES OF Built in ERRORS

# IndexError
# KeyError
# NameError (variable is not defined)
# AttributeError (there are no that attribute in some object)
# NotImplementedError ("This feature has not been implemented yet!")
# RuntimeWarning (Base Error)
# SyntaxError (mess up with Python: missed colons for example)
# IndentationError (spaces for showing scopes)
# TabError (switching between editors, spaces or tabs)
# TypeError (for example can't add string to number)
# ValueError (string can't contain decimal)
# ImportError (importing from each other, circular import)
# DeprecationWarning (no longer the best way of doing something, there is better way)


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make}{self.model}>"


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)


    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Try to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
        self.cars.append(car)
        # raise NotImplementedError('We can not add cars to the garage yet!')


ford = Garage()
car = Car('Ford', 'Fiesta')
ford.add_car("Fiesta")




class UncountableError(ValueError):
    def __init__(self, wrong_value):
        super().__init__(f"Invalid value for n, {wrong_value}. n must be greater than 0.")


# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way
def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)