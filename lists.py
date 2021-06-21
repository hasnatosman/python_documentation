
sqr = [1, 2, 3, 4, 5]
new_sqr = []
for i in sqr:
    i = i ** 2
    new_sqr.append(i)


new_sqr[2] = 6
# list is immutable.............................




print(new_sqr)