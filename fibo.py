a = 0
b = 1
total = []

while a < 1000:
    total.append(a)
    a, b = b, a + b

print(total)
print('Total: ',  len(total))