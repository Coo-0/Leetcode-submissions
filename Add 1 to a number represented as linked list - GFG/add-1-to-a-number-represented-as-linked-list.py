#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        
        curr = head
        last_non_nine = None
        while curr:
            if curr.data != 9:
                last_non_nine = curr
            curr = curr.next
        
        # Increment the rightmost non-nine digit
        if last_non_nine:
            last_non_nine.data += 1
            curr = last_non_nine.next
        else:
            # If all digits are nine, add a new node with value 1 at the beginning
            new_node = Node(1)
            new_node.next = head
            head = new_node
            curr = head.next
        
        # Update all digits after the rightmost non-nine digit to 0
        while curr:
            curr.data = 0
            curr = curr.next
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends