"""This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))
"""

def zero(x = None):
    return 0 if x is None else int(x(0))

def one(x = None):
    return 1 if x is None else int(x(1))

def two(x = None):
    return 2 if x is None else int(x(2))

def three(x = None):
    return 3 if x is None else int(x(3))

def four(x = None):
    return 4 if x is None else int(x(4))

def five(x = None):
    return 5 if x is None else int(x(5))

def six(x = None):
    return 6 if x is None else int(x(6))

def seven(x = None):
    return 7 if x is None else int(x(7))

def eight(x = None):
    return 8 if x is None else int(x(8))

def nine(x = None):
    return 9 if x is None else int(x(9))

def plus(y):
    return lambda x: x + y

def minus(y):
    return lambda x: x - y

def times(y):
    return lambda x: x * y

def divided_by(y):
    return lambda x: x / y