# Given a list of numbers, return the maximum value.

def max_value(nums):
  max=nums[0]
  for i in range(1,len(nums)):
    if nums[i]>max:
      max=nums[i]

  return max



# Test cases
print(max_value([4, 7, 2, 8, 10, 9]))
print(max_value([-5, -2, -1, -11]))