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
        self.next = next # pointer to the next node

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

        
    
    def printed(self):
        if self.head is None: # if there is no head, there is no linked list
            print("The linked list is blank")
            return
        itr = self.head 
        llstr = ""
        while itr: # while there is  a head
            llstr += str(itr.data) + "-> "
            itr = itr.next # this pushes itr into the next node
        print(llstr)

    def sum(self):
        total = 0
        if  self.head is None:
            print("The linked list is blank")
            return
        else:
            itr = self.head
            while itr is not None:
                total += itr.data
                itr = itr.next
        return total

    def find_value(self, value):
        if self.head is None:
            print("There is no node")
            return False
        else:
            itr = self.head
            if itr.data == value:
                return True
            while itr is not None:
                if itr.data == value:
                    return True
                else:
                    itr = itr.next
            return False
    
    def get_node(self, index):
        count = 0
        if self.head is None:
            print("There is no node")
            return None
        if index == count:
            return self.head.data
        else:
            itr = self.head
            while itr is not None:
                if index == count:
                    return itr.data
                count += 1
                itr = itr.next
            return None
  

    def reverse(self): #why does this work
        prev = None # the new node
        current = self.head # the current unreversed node
        while current is not None: # basically we dont have to change the entire head by way of using a list and using the numbers in that list
            #instead, we are changing the nodes to point the opposite direction and have the first node point to None just like the last node
            temp = current.next # the next node is stored temporarily
            current.next = prev # will equal none to start and current later on
            prev = current
            current = temp # goes to the next node
        self.head = prev
'''
Lets use the example linked list of 1 -> 2 -> 3 -> 4 -> 5 -> None
prev is declared as none
current is declared as the head

while there continues to be a node, we will do the following

we declare temp which will be 2
the current.next value is none
prev becomes 1
then we go to the next node by make current temp

temp is 3
current.next is 1
prev becomes 2
then we go to the next node by make current temp

this will go on and on
Prev will start a null and make the start of the list the node connecting to none and the next node connecting to that node
current goes from the start to the end
temp serves as the node value to iterate current
'''



ll = LinkedList()
ll.insert_at_beginning(4)
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_end(5)


# sum = ll.sum()
# print(sum)

# print(ll.find_value(67))

# print(ll.get_node(0))

ll.reverse()
ll.printed()