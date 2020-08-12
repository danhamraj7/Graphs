# understand by looking at test file
# child parent relationship.

# plan
# Graph problem solving
# Translate the problem
# Nodes: the people
# Edge: when a child has a parent.
# Build the Graph || get neighbors

# what algorithm to use
# DFS or BFS will work
# BFS will go to a leaf may be the better choice
##

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    """
    Represent a graph as a dictionary of vertices
    mapping labels to edges.

    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex]

# build a graph


def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(parent, child)
        return graph


def earliest_ancestor(ancestors, starting_node):
    pass
