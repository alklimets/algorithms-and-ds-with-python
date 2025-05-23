'''
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        You must write an algorithm that runs in O(n) time.

        Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

        Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9

        Example 3:
        Input: nums = [1,0,1,2]
        Output: 3

        Constraints:

        0 <= nums.length <= 10^5
        -109 <= nums[i] <= 10^9
'''


def longest_consecutive(nums: list[int]) -> int:
    nums_set = set(nums)
    result = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            current, length = num, 0
            while current in nums_set:
                length += 1
                current += 1
                if length > result:
                    result = length


    return result

print(longest_consecutive([100,4,200,1,3,2]))