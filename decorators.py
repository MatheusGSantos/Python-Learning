"""
    Decorators:
    Functions that takes another function as an argument, adds some funcionality and returns another function, without changing the source code of the argument function
"""

# example
def decorator_f(original_f):
    def wrapper_f():
        print("printed extra stuff") # new functionality
        return original_f()
    return wrapper_f

def display():
    print("display function ran")

display = decorator_f(display)
display()


# now using decorators syntax
@decorator_f # equivalent to display_2 = decorator_f(display_2)
def display_2():
    print("display_2 function ran")

display_2()


"""
    To use decorators to modify single or multiple argument functions, we need to make one little change
"""
# new decorator
def arg_decorator_f(original_f):
    def wrapper_f(*args, **kwargs):
        print("new functionality")
        return original_f(*args, **kwargs)
    return wrapper_f

@arg_decorator_f
def display_info(name, age):
    print(f"name: {name}, age: {age}")

display_info("May", "23")


"""
    We can also use classes as decorators
"""
# declaring a decorator class
class decorator_class(object):
    def __init__(self, original_f):
        self.original_f = original_f

    def __call__(self, *args, **kwargs):
        print('added new functionality')
        return self.original_f(*args, **kwargs)

@decorator_class
def display_3():
    print("this is display_3")

display_3()


"""
    A practical example: get the running time of a function
"""

def function_timer(original_f):
    import time

    def wrapper_f(*args, **kwargs):
        t0 = time.time() # start of the timer
        result = original_f(*args, **kwargs) # running the function and saving the result
        t1 = time.time() - t0 # end of the timer
        print(f"function {original_f.__name__} ran in: {t1} sec")
        return result # returning the result
    
    return wrapper_f

@function_timer
def count_to_n(n):
    counter = 0
    while counter < n:
        counter += 1
    
count_to_n(10000)

"""
    To use multiple decorators in one function, we have to use 'wraps' from functools.
"""

from functools import wraps

def decorator_f1(original_f):
    
    @wraps(original_f) # means that wrapper_f will wrap original_f
    def wrapper_f(*args, **kwargs):
        print("printed extra stuff") # new functionality
        return original_f(*args, **kwargs)
    return wrapper_f


def n_function_timer(original_f):
    import time

    @wraps(original_f)
    def wrapper_f(*args, **kwargs):
        t0 = time.time() # start of the timer
        result = original_f(*args, **kwargs) # running the function and saving the result
        t1 = time.time() - t0 # end of the timer
        print(f"function {original_f.__name__} ran in: {t1} sec")
        return result # returning the result
    
    return wrapper_f

@decorator_f1
@n_function_timer
def print_num(number):
    print(number)


print_num(24)