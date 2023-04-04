# example 3: Anti-patterns/unexpected behavior
from datetime import *


def foo(arg=[]):
    print(arg)

try:
    foo()
except:
    print("caught exception!")
