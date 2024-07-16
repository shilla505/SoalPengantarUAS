def pembagi_indeks(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1

vals = [101, 4, 12, 24]
print(pembagi_indeks(vals, 2))