def addtoarrayform(num, k):
    a = len(num)
    number = 0
    it = 1
    for i in range(a):
        temp = num[-it] * (10 ** i)
        digit = temp
        number = number + digit
        it += 1
    result = str(number + k)
    ar = []
    length = len(result)
    for j in range(length):
        ar.append(int(result[j]))
    return ar


nums = []
add = int(input("Enter add number: "))
le = int(input("Number of elements: "))
for z in range(0, le):
    element = int(input())
    nums.append(element)
print(addtoarrayform(nums, add))
