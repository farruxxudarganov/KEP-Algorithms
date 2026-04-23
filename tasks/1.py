def calc(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        if b == 0:
            return 
        return a / b
    else:
        return

print(calc(10, 2, '+'))
print(calc(10, 2, '*'))