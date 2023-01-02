'''
There are two main types of graphs. One is an undirected graph. There is also a directed graph.
Graph vs tree: a graph can have multiple paths two a node while a tree can only have one.
A use case of graph data structures is to find the shortest/best route to travel on to get to a certain position or instagram follow recommendations.
                  Tree                                    Graph

                  8                                        Italy \
                /   \                                              Ukraine
               6      15                                   London /
              /  \    /  \
             2    7   12  23

A graph could be weighted based on distance
In python, we will use sets or even dictionaries (hashmaps)
'''

# class Graph:
#     def __init__(self, edges):
#         self.edges = edges
#         self.graph_dict = {}
#         for start, end in self.edges:
#             if start in self.graph_dict:
#                 self.graph_dict[start].append(end)
#             else:
#                 self.graph_dict[start] = [end] # note that they should already be in a dictionary
        
#     def get_paths(self, start, end, path=[]):
#         path = path + [start]

#         if start not in self.graph_dict:
#             return []

#         if start == end:
#             return path
        
#         paths = []

#         for node in self.graph_dict[start]:
#             if node not in path:
#                new_paths = self.get_paths(node, end, path)
#                for p in new_paths:
#                 paths.append(p)
#         return paths

#     def get_shortest_paths(self, start, end, path=[]):

#         path = path + [start]
#         paths = []

#         if start not in self.graph_dict:
#             return None
        
#         if start == end:
#             return path

#         shortest_path = None
#         for node in self.graph_dict[start]:
#             if node not in path:
#                sp = self.get_shortest_paths(node, end, path)
#                if sp:
#                 if shortest_path is not None or len(sp) < len(shortest_path):
#                     shortest_path = sp
#         return shortest_path

        


# routes = [
#     ("Mumbai", "Paris"),
#     ("Mumbai", "Dubai"),
#     ("Paris", "Dubai"),
#     ("Paris", "New York"),
#     ("Dubai", "New York"),
#     ("New York", "Toronto"),
# ]

# graph = Graph(routes)






graph = {}

graph["a"] = ["c", "b"]
graph["b"] = ["d"]
graph["c"] = ["e"]
graph["d"] = ["f"]
graph["e"] = []
graph["f"] = []

'''
Depth First traversal would follow a pattern of going through a graph. <- Stack (Add from the top / remove from the top FIFO) *Think of a stack vertically*
Breadth First traversal would start at one node and then go through all neighbor nodes before going to the next node. <- Queue (Add to back and remove from the front LIFO) *think of a queue horizontally*
'''

def depthFirstPrint(graph, source): # the parameters are the graph (the nodes) and one single key of the graph
    stack = [source] # we instantiate a stack with the starting node of source
    
    while len(stack) > 0:
        current = stack.pop() # this will take out the last node and make current the value of the last ndoe
        print(current)
        # this will make current the last element of the array. It wont actually take it out of the stack.
        # we would then want to add the neighbor nodes to the stack and then take out the current node.
        # the next iteration would then start
        for neighbor in graph[current]:
            stack.append(neighbor)

def breadthFirstPrint(graph, source):
    queue = [source]
    while len(queue) > 0: 
        current = queue.pop(0) # this is the only difference betwwen depth and breadth. We remove the 0th element or the front
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

def recursivePrint(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursivePrint(graph, neighbor)

        
# def hasPath(graph, source, goal): # we want to see if there is or is not a path from the source or start to the goal or end
#     # this is a recursive function so we should start off with a base case
#     if source == goal:
#         return True
#     for neighbor in graph[source]:
#         if hasPath(graph, neighbor, goal) == True:
#             return True
#     return False

# def hasPath(graph, source, goal): # this is the iterative way of hasPath(). It can  also be done with a queue
#     stack = [source]

#     while len(stack) > 0:
#         current = stack.pop()
#         if current == goal:
#             return True
#         for neighbor in graph[current]:
#             stack.append(neighbor)
    
#     return False

def hasPath(graph, source, goal): # this is the iterative way of hasPath() while using a queue
    queue = [source]

    while len(queue) > 0:
        current = queue.pop(0)
        if current == goal:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False



# depthFirstPrint(graph, "a")
# breadthFirstPrint(graph, "a")
recursivePrint(graph, "a")
# print(hasPath(graph, "a", "e"))
