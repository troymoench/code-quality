# example 3: Anti-patterns/unexpected behavior
from datetime import *

print("The day is", date.today())


def foo(arg=[]):
    print(arg)
