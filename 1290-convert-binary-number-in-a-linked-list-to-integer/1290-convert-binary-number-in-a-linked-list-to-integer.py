# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
          
        decnum=0
        power=len(arr)-1
        for i in arr:
            decnum+=i * (2**power)
            power-=1
            
        return decnum