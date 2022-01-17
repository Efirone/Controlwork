def decorator(func):
    def wrapper(v,v0,t):
        try:
            a=(v-v0)/t
        except TypeError:
            print('переменные не числа')
            v=10
            v0=5
            t=2
        except ZeroDivisionError:
            print('время не может быть 0')
            t=2
        a=func(v,v0,t)
        S=(v0*t)+(a*t*t)/2
        print(S)
    return wrapper
@decorator
def func(v,v0,t):
    a=(v-v0)/t
    return a
func(143,'5fad',12)
