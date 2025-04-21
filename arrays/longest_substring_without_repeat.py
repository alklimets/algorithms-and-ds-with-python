'''
        Given a string s, find the length of the longest substring without duplicate characters.

        Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Constraints:

        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols and spaces.
'''


def length_of_longest_substring(s: str) -> int:
    window = set()
    left, result = 0, 0
    for i in range(len(s)):
        ch = s[i]
        while ch in window:
            l_ch = s[left]
            window.remove(l_ch)
            left += 1
        window.add(ch)
        result = max(result, len(window))
    return result
