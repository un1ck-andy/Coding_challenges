def fibo(x):
    a, b = 0, 1
    for i in range(x):
        yield a
        a, b = b, a+b


print(list(fibo(100)))
