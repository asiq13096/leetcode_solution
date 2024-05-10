def removeduplicates(nums):
    j = 0
    expected_nums = []
    l = len(nums)
    while j in range(l - 1):
        if nums[j] != nums[j + 1]:
            expected_nums.append(nums[j])
        j += 1
    if nums[j] == nums[l - 1]:
        expected_nums.append(nums[l - 1])
    value = len(expected_nums)
    i = 0
    for i in range(value):
        nums[i] = expected_nums[i]
    return len(nums)


a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeduplicates(a)
print(k)
