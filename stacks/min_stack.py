'''
        Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

        Implement the MinStack class:
        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.
        You must implement a solution with O(1) time complexity for each function.

        Example 1:

        Input
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

        Output
        [null,null,null,null,-3,null,0,-2]

        Explanation
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin(); // return -3
        minStack.pop();
        minStack.top();    // return 0
        minStack.getMin(); // return -2


        Constraints:

        -2^31 <= val <= 2^31 - 1
        Methods pop, top and getMin operations will always be called on non-empty stacks.
        At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
'''

class Node:
    def __init__(self, val, min_val, nxt):
        self.val = val
        self.min_val = min_val
        self.nxt = nxt


class MinStack:

    def __init__(self):
        self.node = None

    def push(self, val: int) -> None:
        min_val = min(val, self.node.min_val) if self.node else val
        self.node = Node(val, min_val, self.node)

    def pop(self) -> None:
        self.node = self.node.nxt

    def top(self) -> int:
        return self.node.val

    def get_min(self) -> int:
        return self.node.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())
min_stack.pop()
print(min_stack.get_min())
