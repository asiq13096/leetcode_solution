def ispalindrome(a):
    temp = a
    r = 0
    while a > 0:
        digit = a % 10
        r = r * 10 + digit
        a = a // 10
    if temp == r:
        return True
    else:
        return False


q = int(input("Enter a number: "))
print(ispalindrome(q))
