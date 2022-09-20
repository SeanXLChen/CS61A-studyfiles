def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped

#triple = trace(triple)
@trace
def triple(x):
    print(3 * x)
    return 3 * x

triple(30)