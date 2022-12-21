'''
Why use linked list over a normal array?
When we want to add an element to an array that has max capacity, we have to make a new capacity and re-add all of the previous elements.
This makes it take more time than using a linked list.
If we want to add an element to a linked list, we only need to change the pointers of 1 node. This is much faster.
The time complexity to insert an element at the beginning of the linked list is O(1) or constant time.
The time complexity to delete an element at the beginning of the linked list is O(1) or constant time.
The time complexity to insert/delete an element at the end of the linked list is O(n) or linear time.
*YOU DON'T NEED ALLOCATE SPACE*
Traversal is O(n)
Accessing an element by a certain value is also O(n)

A downside to linked lists is that it takes O(n) time to  index each element while an array is constant time if a user knows where they want to index at. linkedList[5] is not a thing.
'''

class Node:
    def __init__(self, data=None, next=None): # every node has data like a number for example. It then has a pointer to the next node
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None # the head of the linked list is the first node

    def insert_at_beginning(self, data):
        node = Node(data, self.head) # this will create a node and then make the head or first node of linked list into that node. The head is theaargument for the next parameter. 
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None: # if there is no head, that means there is no linked list. 
            self.head = Node(data, None) # We would then add the node with no pointer because there is nothing else
            return
        itr = self.head
        while itr.next: # if there is a head, we will iterate through the linked list until iterator can't find a next node
            itr = itr.next
        itr.next = Node(data, None) # we will then add a next node with the given input

        
    
    def print(self):
        if self.head is None: # if there is no head, there is no linked list
            print("The linked list is blank")
            return
        itr = self.head 
        llstr = ""
        while itr: # while there is  a head
            llstr += str(itr.data) + "-> "
            itr = itr.next # this pushes itr into the next node
        print(llstr)




ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(89)
ll.insert_at_end(69)
ll.print()




