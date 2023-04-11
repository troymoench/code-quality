# example 2: undefined variable error (runtime exception)
from datetime import datetime

hello = "world"

if hello == "world":
    print("Hello", hello)

print("The time is", datetime.now())
