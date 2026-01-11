def add_numbers(a, b):
    c = a + b
    return c

def unused_function():
    x = 10  # pylint should warn about this

print(add_numbers(2, 3))

