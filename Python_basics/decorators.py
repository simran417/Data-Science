# timing function execution:
'''import time
def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start}")
        return result
    return wrapper

@timer #decorator
def ex_fn(n):
    time.sleep(n)

ex_fn(2)'''

# cache memory:
import time
def cache(func):
    cache_value={}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def sum(a, b):
    time.sleep(4)
    return a+b

print(sum(2, 3))
