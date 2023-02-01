# Define a function f taking x
# and returning x^2.
def f(x):
    return x ** 2


# Define a function g taking x and y
# and returning 4x^2 + y^2.
def g(x, y):
    return 4 * x ** 2 + y ** 2

# Sees that '4 * x ** 2 + y ** 2'
# does not need parentheses.


if __name__ == '__main__':
    print(f(2))
    print(f(3))
    print(f(-2))

    print()

    print(g(4, 5))
