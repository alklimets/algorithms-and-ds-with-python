'''
        Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
        A subarray is a contiguous non-empty sequence of elements within an array.

        Example 1:
        Input: nums = [1,1,1], k = 2
        Output: 2

        Example 2:
        Input: nums = [1,2,3], k = 3
        Output: 2

        Constraints:

        1 <= nums.length <= 2 * 10^4
        -1000 <= nums[i] <= 1000
        -107 <= k <= 10^7
'''

def subarray_sum(nums: list[int], k: int) -> int:
    prefix_sum = 0
    counts = {0: 1}
    result = 0
    for i, val in enumerate(nums):
        prefix_sum += val
        if (prefix_sum - k) in counts:
            result += counts[prefix_sum - k]
        counts[prefix_sum] = counts.get(prefix_sum, 0) + 1

    return result


print(subarray_sum([1, 1, 1], 2))