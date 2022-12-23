'''
One example of a tree is a category system in Amazon.
Click on electronics. This will take you to a category of phones, laptops, TVs, etc.
Click on TVs and then you will see a list view of all the TVs. This can go deeper and deeper

A tree is a recursive data structure. Every child node is a tree itself.
'''

class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self # This will add the current node as a parent node of the created child node
        self.children.append(child) # this will append a child tree to the children list  of another Tree

    
    def get_level(self):
        level = 0
        p = self.parent
        while p is not None:
            level += 1
            p = p.parent
        return level

    
    def print_children(self):
        spaces = " " * self.get_level() * 4
        print(spaces + self.value) # prints the value
        if len(self.children) > 0: # if there are children, print the children and then print children will be called to the children which will print and so on 
            for child in self.children:
                child.print_children()


tree = Tree("Sale")


c1 = Tree("Electronics")
c1.add_child(Tree("Phone"))
c1.add_child(Tree("Computer"))
c1.add_child(Tree("Monitor"))


c2 = Tree("Manga")
c2.add_child(Tree("Bleach"))
c2.add_child(Tree("Dr. Stone"))
c2.add_child(Tree("Blue Lock"))

tree.add_child(c1)

tree.add_child(c2)

tree.print_children()

c2.get_level()