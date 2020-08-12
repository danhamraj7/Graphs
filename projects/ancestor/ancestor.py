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
        if v1 in self.vertices and v2 in self.vertices:
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
    graph = build_graph(ancestors)

    # make a stack
    s = Stack()
    # make a set for visited
    visited = set()
    # push A PATH TO the starting_vertex
    s.push([starting_node])
    # As we traverse through keep track of longest path
    longest_path = []
    # earliest ancestor
    aged_one = -1
    # while the stack is not empty
    while s.size() > 0:
        # pop  the  path
        path = s.pop()
        # current node is the last thing in the path
        current_node = path[-1]
        # check if the current node is the one we want
        # if path is longer or path is equal but the id is smaller
        if (len(path) >= len(longest_path) and current_node < aged_one or len(path) > len(longest_path)):
            longest_path = path
            # the last thing in the path
            aged_one = longest_path[-1]

            if current_node not in visited:
                # add it
                visited.add(current_node)

                parents = graph.get_neighbors(current_node)

                for parent in parents:
                    new_path = path + [parent]
                    s.push(new_path)
            return longest_path[-1]
