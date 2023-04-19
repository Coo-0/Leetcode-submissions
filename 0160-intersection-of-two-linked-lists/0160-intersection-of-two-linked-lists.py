# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lenA=0
        lenB=0
        currA=headA
        currB=headB
        
        while currA:
            lenA+=1
            currA=currA.next
            
        while currB:
            lenB+=1
            currB=currB.next
          
        currA=headA
        currB=headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                currA=currA.next
        if lenB>lenA:
            for i in range(lenB-lenA):
                currB=currB.next
            
        while currA!=currB:
            currA=currA.next
            currB=currB.next
            
        return currA
            