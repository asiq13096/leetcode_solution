def f(nums):
    x = len(nums)
    d = 0
    for n in range(x - 1 or x):
        if not nums:
            break
        if len(nums) >= 2:
            a = nums[0]
            b = nums[len(nums) - 1]
            c = int(str(a) + str(b))
        else:
            a = nums[0]
            b = 0
            c = int(str(a))
        d = d + c
        c = 0
        nums.pop(0)
        if len(nums) >= 2:
            nums.pop(len(nums) - 1)
        else:
            break
    print("Concatenation Result: ", d)


num = []
length = int(input("Number of elements: "))
for i in range(0, length):
    element = int(input())
    num.append(element)
f(num)
