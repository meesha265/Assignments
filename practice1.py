from functools import wraps

def multiplier(func):
    @wraps(func)
    def times(*args, **kwargs):
        no = args[0]
        if not isinstance(no, int) and not isinstance(no, float):
            raise ValueError

        print(f"{func.__name__} was applied to {args=} and {kwargs=}")
        return func (*args, **kwargs)
    return times

@multiplier
def multiples(no):
    return no ** 10

ans = multiples(3)
print(ans)