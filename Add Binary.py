def addbinary(a, b):
    a = int(input(), 2)
    b = int(input(), 2)
    d = str(format(a + b, 'b'))

    return d


x = 0
y = 0
print(addbinary(x, y))