# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head

        while (head and head.val == val):
            head = head.next  
        
        cur = head
        while cur:
            if (cur.next == None):
                break
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next  
              
        return head
