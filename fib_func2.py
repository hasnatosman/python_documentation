def fibo(n):
    fibo_list = []
    a, b = 0, 1
    while a < n:
        fibo_list.append(a)
        a, b = b, a + b
    return fibo_list


x = fibo(100)
print('Fibonacci series: ', x)
