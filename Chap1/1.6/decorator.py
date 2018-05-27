
def trace1(fn):
    def wrapped(x):
        print('calling function {} on argument {}'.format(fn, x))
        return fn(x)
    return wrapped

@trace
def triple(x):
    return x**3


