# example 3: Anti-patterns/unexpected behavior
from datetime import date

print("The day is", date.today())


def foo(arg=None):
    if arg is None:
        arg = []
    print(arg)
