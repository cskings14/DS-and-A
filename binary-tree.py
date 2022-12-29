'''
A binary tree is just a generic tree with the requirement that there are at most two child nodes.
A binary search tree is a binary tree with the requirement that the element have an order and all elements are unique.
A BST example could be the number 50 as the root node (level 0 or L0) with nodes lower than 50 to the left and nodes higher than 50 to the right.
The time complexity to search for a number would be O(logn) because the the BST will halved every iteration down the tree.

The two main traversal techniques are Breadth First Search and Depth First Search (Inorder traversal, preorder traversal, and postorder traversal).

             15
            /  \
           12   27
          / \   / \
         7  14 20  88
                \
                23

in order traversal: [7, 12, 14, 15, 20, 23, 27, 88] Goes from lowest to highest node value starting at the lowest value node.
pre order traversal: [15, 12, 7, 14, 27, 20, 23, 88] Goes from left to right starting at the root node going left. 
^THIS IS THE SAME AS DEPTH FIRST^
post order traversal: [7, 14, 12, 23, 20, 88, 27, 15] Goes from left sub tree to right sub tree (from left to right) and ends with the root node.
Breadth first traversal: [15, 12, 27, 7, 14, 20, 88, 23] Goes from left to right starting up and going down.
'''

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # there are no duplicates
        elif data < self.data:
            if self.left:
                self.left.add_child(data) # this will make a child of an already existing child
            else:
                self.left = BST(data) # makes a bst node with the data if there is no child already
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data) # makes a bst node with the data if there is no child already
    
    def inorder_traversal(self):
        elements = []

        # visits left tree
        if self.left:
            elements += self.left.inorder_traversal() # this will find the lowest left element
        
        elements.append(self.data) # this will add the root node

        # visits right tree
        if self.right:
            elements += self.right.inorder_traversal() # this will find the highest right element
        
        return elements

    def bfs(self, root):
        if root is None:
            return
        queue = [root]

        while len(queue) > 0:
            cur_node = queue.pop(0)

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)

            # end

    def preorder_traversal(self, root): # we need a root to use recursion properly
        # if root is None,return
        if root is None:
            return
        # print the current node
        print(root.data, end=", ")
        # traverse left subtree
        self.preorder_traversal(root.left) # 

        # traverse right subtree
        self.preorder_traversal(root.right)

    def build_tree(elements):
        root = BST(elements[0]) # sets the first value to the root node
        for i in range(1, len(elements), 1):
            root.add_child(elements[i]) # uses the add child functionality to add the elements
        return root
    
    def search(self, value):
        if value == self.data: # if the value is equal to the root iteration (it can be a different node just at the recursive start) return true
            return True
        elif value < self.data: 
            if self.left:
                return self.left.search(value) # if the value to search is less than the root iteration, it will recursively go to that iteration
            return False # it will return false if the searched value is lower than any given left node
        elif value > self.data:
            if self.right:
                return self.right.search(value) # if the value to search is greater than the root iteration, it will recursively go to that iteration
            return False # it will return false if the searched value is higher than any given right iteration
        else:
            return False # if none of the above, just return false

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
        
        min_val = self.right.find_min()
        self.data = min_val
        self.right = self.right.delete(min_val)

        return self



numbers = [17, 4, 4, 1, 20, 9, 23, 18, 34, 18, 14]
tree = BST.build_tree(numbers)
print(tree.inorder_traversal())
print(tree.search(17))



nums = [15, 7, 12, 14, 20, 23, 27, 88]
tre = BST.build_tree(nums)
print(tre.preorder_traversal(tre))
