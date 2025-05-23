from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev