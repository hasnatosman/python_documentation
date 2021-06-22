def fibo(n):
    x, y = 0, 1
    while x < n:
        print(x, end='\n')
        x, y = y, x + y


fibo(2000)
