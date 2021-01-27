nums = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
increasing_nums = list(nums)
print(nums)
increasing_nums.sort()
print(increasing_nums)
decreasing_nums = list(increasing_nums)
decreasing_nums.reverse()
print(decreasing_nums)
print(increasing_nums[1::2])
print(increasing_nums[::2])
print(increasing_nums[2::3])

