"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue the starting node
        q.enqueue(starting_vertex)
        # make a set to track if we being here before.
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue whatever is at the front of the line
            # (this is the current node)
            current_node = q.dequeue()
        # if the curr_node is a node that was
        # not visited
        if current_node not in visited:
            print(current_node)
            # add it to visited
            visited.add(current_node)
        # get the nodes that it is connected to.
            neighbors = self.get_neighbors(current_node)
        # for each of those nodes
            for neighbor in neighbors:
                # add them to the queue
                q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push onto our starting node
        s.push(starting_vertex)
        # make a set to track if we visited that node before
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop off whatever is at the top(This is the current node.)
            current_node = s.pop()
        # if we have not visited that node before
            if current_node not in visited:
                # run fn and print current node
                print(current_node)
        # # we mark it as visited
                visited.add(current_node)
        # we then get each of the node it is connected to
                neighbors = self.get_neighbors(current_node)
        # for each in the nodes that is connected(neighbors)
                for neighbor in neighbors:
                    # push it to the stack.
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # make a set for visited
        visited = set()
        # enqueue A PATH TO the starting_vertex
        q.enqueue([starting_vertex])
        # while the stack is not empty
        while q.size() > 0:
            # dequeue the next path(current path)
            current_path = q.dequeue()
            # current node is the last thing in the path
            current_node = current_path[-1]
            # check if the current node is the one we want
            if current_node == destination_vertex:
                # return it
                return current_path

            else:
                # if the current node is not in the visited
                if current_node not in visited:
                    # add it to visited
                    visited.add(current_node)
                    # get the nodes that is connected to curr node
                    edges = self.get_neighbors(current_node)
                    # loop over edges
                    for edge in edges:
                        # make a list with the paths
                        path_copy = list(current_path)
                        # append the path to the list
                        path_copy.append(edge)
                        # enqueue fn and pass in path copy
                        q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
