from collections import defaultdict

'''
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
        
        Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        
        Example 2:
        Input: nums = [1], k = 1
        Output: [1]
        
        Constraints:
        
        1 <= nums.length <= 10^5
        -104 <= nums[i] <= 10^4
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.
         
        
        Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    nums_frequencies = defaultdict(int)
    for val in nums:
        nums_frequencies[val] += 1

    frequency_items = defaultdict(list)
    for key, val in nums_frequencies.items():
        frequency_items[val].append(key)

    result = []
    for fr in sorted(frequency_items.keys(), reverse=True):
        for item in frequency_items[fr]:
            result.append(item)
            k -= 1
            if k == 0:
                return result
    return result


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))