lst = [1, 7, 4, 6, 2, 9, 12, 4, 44, 56, 1, 5]
s = 0

for i in lst:
    if i < 30 and i % 3 == 0:
        print(i)
    else:
        s += i

print(s)