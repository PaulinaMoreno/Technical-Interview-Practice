import unittest
from collections import defaultdict
'''
Question 3
Given an undirected graph G, find the minimum spanning tree within G.
A minimum spanning tree connects all vertices in a graph with the
smallest possible total weight of edges. Your function should
take in and return an adjacency list structured like this:

{'A': [('B', 2)],
'B': [('A', 2), ('C', 5)],
'C': [('B', 5)]}
'''

# Graph representation


class Graph:

    def __init__(self, vertices):
        self.V = vertices   # number of vertices
        self.graph = []   # graph dictonary

    # Add edge to graph
    # @param {string,string,string} vertex u , vertex v, weight

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Union of sets of x and y by rank
    # @param {list,list,string, string}

    def union(self, parent, rank, x, y):
        indexX = self.find(parent, x)
        indexY = self.find(parent, y)

        # add a smaller rank tree under root of a high rank tree
        if rank[indexX] < rank[indexY]:
            parent[indexX] = indexY
        elif rank[indexY] > rank[indexX]:
            parent[indexY] = indexX

        # If ranks are equal, make one index X or Y root and
        # increment its rank in 1

        else:
            parent[indexY] = indexX
            rank[indexX] += 1

    # Find set of element x
    # @param {list,string}
    def find(self, parent, x):
        if parent[x] == x:
            return x
        return self.find(parent, parent[x])

    # Function to construct MST (Kruskal's algorithm)
    # @return {list} mst graph
    def KruskalMST(self):

        output_graph = []
        # order graph in ascending order by weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # add vertex to parent list
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        i = 0
        numberV = 0
        while numberV < self.V - 1:
            # pickup the smallest element in graph
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If not cycle, append it to result and increment e
            if x != y:
                numberV += 1
                output_graph.append([u, v, w])
                self.union(parent, rank, x, y)

        return output_graph

# Validate input graph
# @param {dict} input graph
# @return {boolean}, True is the graph is valid


def validateG(G):
    # check if G is dictionary
    if type(G) != dict:
        return "G is not dictionary!"
    # check if G have more than one node
    if len(G) < 2:
        return "G has not enough vertices"
    return True

# Validate input graph
# @param {dict} input graph
# @return {boolean}, True is the graph is valid


def question3(G):
    if validateG(G):

        vertex_dict = {}  # dict for store vertices - index relationship 'A'-0
        inverted_dict = {}  # dict for store index -vertices relationship 0-'A'
        count = 0
        # Get  vertices
        vertices = G.keys()
        graph = Graph(len(vertices))

        # Give at each vertex a number
        for i in G:
            vertex_dict[i] = count
            inverted_dict[count] = i
            count += 1
        # Add edges to the graph
        for i in vertices:
            for j in G[i]:
                u, v, w = vertex_dict[i], vertex_dict[j[0]], j[1]
                graph.addEdge(u, v, w)

        mst = graph.KruskalMST()
        # Create adj list response
        output_graph = {}
        for i in mst:
            if inverted_dict[i[0]] in output_graph:
                output_graph[inverted_dict[i[0]]].append((inverted_dict[i[1]], i[2]))  # noqa
            else:
                output_graph[inverted_dict[i[0]]] = [(inverted_dict[i[1]], i[2])]  # noqa

            if inverted_dict[i[1]] in output_graph:
                output_graph[inverted_dict[i[1]]].append((inverted_dict[i[0]], i[2]))  # noqa
            else:
                output_graph[inverted_dict[i[1]]] = [(inverted_dict[i[0]], i[2])]  # noqa
    return output_graph


def Q3Test():
        G = {'A': [('B', 2)],
             'C': [('B', 5)],
             'B': [('A', 2), ('C', 5)]}

        if question3(G) == G:
            print('True')
        else:
            print('False')

if __name__ == '__main__':
    Q3Test()
