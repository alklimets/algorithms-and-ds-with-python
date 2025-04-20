'''
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation.

        Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

        Constraints:

        2 <= nums.length <= 10^5
        -30 <= nums[i] <= 30
        The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
        Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''


def product_except_self(nums: list[int]) -> list[int]:
    prefix_product = [1] * len(nums)
    for i in range(1, len(nums)):
        prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

    prefix = 1
    for i in range(len(nums) - 1, -1, -1):
        prefix_product[i] *= prefix
        prefix *= nums[i]
    return prefix_product

# faster
def product_except_self2(nums: list[int]) -> list[int]:
    product, zeros = 1, 0
    for num in nums:
        if num != 0:
            product *= num
        else:
            zeros += 1
    if zeros > 1: return [0] * len(nums)

    res = [1] * len(nums)
    for i, num in enumerate(nums):
        if zeros:
            res[i] = 0 if num != 0 else product
        else:
            res[i] = product // num
    return res

print(product_except_self([1, 2, 3, 4]))
print(product_except_self2([1, 2, 3, 4]))