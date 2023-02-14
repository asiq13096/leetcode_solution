def twosum(nums, target):
    indices = []
    a = len(nums)
    for i in range(a):
        for j in range(i + 1, a):
            if nums[i] + nums[j] == target:
                for index, value in enumerate(nums):
                    if index == j:
                        indices.append(index)
                    elif index == i:
                        indices.append(index)
    return indices


num = []
number = int(input("Target Number: "))
length = int(input("Number of elements: "))
for n in range(0, length):
    element = int(input())
    num.append(element)
another = twosum(num, number)
print(another)

"""New"""
