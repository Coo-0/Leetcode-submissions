#User function Template for python3

"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def partition(self, head, x):
        before_x = before_x_head = Node(0)
        equal_x = equal_x_head = Node(0)
        after_x = after_x_head = Node(0)
        
        # Traverse the linked list and insert nodes into appropriate partition
        while head:
            if head.data < x:
                before_x.next = head
                before_x = before_x.next
            elif head.data == x:
                equal_x.next = head
                equal_x = equal_x.next
            else:
                after_x.next = head
                after_x = after_x.next
            head = head.next
        
        # Join the three partitions
        after_x.next = None
        equal_x.next = after_x_head.next
        before_x.next = equal_x_head.next
        
        # Return the head of the partitioned linked list
        return before_x_head.next


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.partition(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends