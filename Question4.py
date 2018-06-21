import Queue
import unittest
'''
Question 4
Find the least common ancestor between two nodes on a binary search tree.
The least common ancestor is the farthest node from the root that is
an ancestor of both nodes. For example, the root is a common ancestor
of all nodes on the tree, but if both nodes are descendents of the
root's left child, then that left child might be the lowest common
ancestor. You can assume that both nodes are in the tree,
and the tree itself adheres to all BST properties.
The function definition should look like question4(T, r, n1, n2), where T
is the tree represented as a matrix, where the index of the list is equal
to the integer stored in that node and a 1 represents a child node,
r is a non-negative integer representing the root, and n1 and n2
are non-negative integers representing the two nodes in no particular
order. For example, one test case might be

'''


class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.right = None
        self.left = None
    # Function to insert a new node to the right

    def child_right(self, data):
        new_node = Node(data)
        self.right = new_node
        return new_node

    # Function to insert a new node to the left

    def child_left(self, data):
        new_node = Node(data)
        self.left = new_node
        return new_node

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def getData(self):
        return self.data


# Function to find LCA of n1 and n2.
# both n1 and n2 are present in BST
# @param {Node,int,int} root Node, n1 , n2
# @return {Node}, LCA


def LCA(root, node1, node2):
    # Basic case
    if root is None:
        return None
    if root.data < node1 and root.data < node2:
        return LCA(root.right, node1, node2)
    if root.data > node1 and root.data > node2:
        return LCA(root.left, node1, node2)
    return root

# Construct the BST
# @param {Matrix, Node,int,int} Tree represented as a matrix,
# root Node, n1 , n2
# @return {Node}, root of BST


def question4(T, r, n1, n2):
    root = Node(r)
    size_matrix = len(T)
    q = Queue.Queue()
    q.put(root)
    # Use a Queue to construct the BST

    while not q.empty():
        node = q.get()
        for x in range(0, node.getData()):
            if T[node.getData()][x] == 1:
                q.put(node.child_left(x))
        for y in range(node.getData(), size_matrix):
            if T[node.getData()][y] == 1:
                q.put(node.child_right(y))
    return root


class Q4Test(unittest.TestCase):
    def test(self):
        head = question4([[0, 1, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [1, 0, 0, 0, 1],
                         [0, 0, 0, 0, 0]],
                         3,
                         1,
                         4)
        lca_node = LCA(head, 1, 0)
        self.assertEqual(lca_node.getData(), 0)
        lca_node2 = LCA(head, 1, 4)
        self.assertEqual(lca_node2.getData(), 3)
        self.assertNotEqual(lca_node2.getData(), 2)


if __name__ == '__main__':
    unittest.main()
