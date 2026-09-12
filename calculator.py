def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b  # bug: doesn't handle b == 0, raises ZeroDivisionError

def average(numbers):
    return sum(numbers) / len(numbers)  # same bug: empty list crashes this