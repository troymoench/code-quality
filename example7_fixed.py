# example 7: complexity


def foo(a, b, c, d, e):
    if not a:
        return 6
    if not b:
        return 5
    if not c:
        return 4
    if not d:
        return 3
    return 2 if not e else 1
