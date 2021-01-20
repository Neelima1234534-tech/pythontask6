#DECORATORS
Decorators are a way to change, enhance or alter in any way how a function works.

Decorators are defined with the @ symbol followed by the decorator name, just before the function definition.

Example:

@logtime
def hello():
    print('hello!')
This hello function has the logtime decorator assigned.

Whenever we call hello(), the decorator is going to be called.

A decorator is a function that takes a function as a parameter, wraps the function in an inner function that performs the job it has to do, and returns that inner function. In other words:

def logtime(func):
    def wrapper():
        # do something before
        val = func()
        # do something after
        return val
    return wrapper
