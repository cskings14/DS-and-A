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

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end] # note that they should already be in a dictionary
        
    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start not in self.graph_dict:
            return []

        if start == end:
            return path
        
        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
               new_paths = self.get_paths(node, end, path)
               for p in new_paths:
                paths.append(p)
        return paths

    def get_shortest_paths(self, start, end, path=[]):

        path = path + [start]
        paths = []

        if start not in self.graph_dict:
            return None
        
        if start == end:
            return path

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
               sp = self.get_shortest_paths(node, end, path)
               if sp:
                if shortest_path is not None or len(sp) < len(shortest_path):
                    shortest_path = sp
        return shortest_path

        


routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

graph = Graph(routes)