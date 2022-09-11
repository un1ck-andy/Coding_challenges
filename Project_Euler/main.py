arr = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        arr.append(i)
print(sum(arr))



def fibo(x):
    a, b = 0,1
    for i in range(x):
        yield a
        a, b = b, a + b
        if a > 4000000:
            return a
def summ(x):
    lst = []
    for i in list(fibo(x)):
        if i % 2 == 0:
            lst.append(i)
    return sum(lst)

print(summ(4000000))