'''
A stack is a LIFO (last in first out) data structure.
Pushing/popping has a time complexity of O(1)
searching an element by a value is O(n)

One use case could be a back/forward system for the urls of a browser.
Another use case is when a function calling a function. The compiler or interpreter may be using a stack.
CTRL + Z is an example operation of a stack

In python, we can use a list for a stack
'''

s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')
print(s.pop())