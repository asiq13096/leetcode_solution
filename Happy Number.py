def happy(number):
    n = str(number)
    b = 0
    for j in range(1000):
        for i in n:
            b += int(i) ** 2
        if b == 1:
            return True
        else:
            n = str(b)
            b = 0
    return False


k = int(input("Enter a number: "))
print(happy(k))

"""
Better Approach:

class Solution:
    def isHappy(self, n):
        cache = set()
        def happyHelper(n):
            if n == 1:
                return True
            if n in cache: 
                return False
            else:
                cache.add(n)
                dSum = 0
                while n > 0:
                    n, digit = divmod(n, 10)
                    dSum += digit**2
                return happyHelper(dSum)
        return happyHelper(n)

"""