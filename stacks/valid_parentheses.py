'''
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

        Example 1:
        Input: s = "()"
        Output: true

        Example 2:
        Input: s = "()[]{}"
        Output: true

        Example 3:
        Input: s = "(]"
        Output: false

        Example 4:
        Input: s = "([])"
        Output: true

        Constraints:

        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.
'''


def is_valid(s: str) -> bool:
    stack = []
    parentheses = {')' :'(', '}' :'{', ']' :'['}

    for p in s:
        if p in parentheses.values():
            stack.append(p)
        else:
            if not stack or parentheses[p] != stack[-1]:
                return False
            stack.pop()
    return not stack

print(is_valid('()[]{}'))