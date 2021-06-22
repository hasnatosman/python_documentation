for n in range(2, 10):
    print(n)
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x,'It ia an odd number!')
            break
    else:
        print(n, 'is a prime number!')
print()
print('Done !!')
