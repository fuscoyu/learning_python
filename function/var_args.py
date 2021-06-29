def print_multiple_args(*args):
    print(type(args), args)
    for idx, val in enumerate(args):
        print(idx, val)

#print_multiple_args('a', 'b', 'c')

def print_kwargs(**kwargs):
    print(type(kwargs), kwargs)
    for k, v in kwargs.items():
        print('{}: {}'.format(k, v))

#print_kwargs(a=1, b=2)

def print_all(a, *args, **kwargs):
    print(a)
    if args:
       print(args)
    if kwargs:
       print(kwargs)

print_all('hello', 'world', b = 10)
