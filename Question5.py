import unittest
""" Find the element in a singly linked list that's m elements
from the end. For example, if a linked list has 5 elements, the
3rd element from the end is the 3rd element. The function definition
should look like question5(ll, m), where ll is the first node of a linked
list and m is the "mth number from the end". You should copy/paste the
Node class below to use as a representation of a node in the l
inked list. Return the value of the node at that position.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    # Insert at the end

    def insertNode(self, data):
        new_node = Node(data)

        if self.head == None:  # noqa
            self.head = new_node
        else:
            current = self.head
            while current.next != None:  # noqa
                current = current.next
            current.next = new_node

    def length(self):

        current = self.head
        if self.head == None:  # noqa
            return 0
        else:
            count = 1
            while current.next != None:  # noqa
                count += 1
                current = current.next
            return count

    def printList(self):
        node = self.head
        print(str(node.data)+(' head'))
        while node:
            print(node.data)
            node = node.next

    # Function to find the mth node in the list
    # @param {int} mth node
    # @return {int}, mth node data

    def findMthNode(self, data):
        size = self.length()
        count = 1
        node = self.head
        if data > size or data <= 0:
            return -1
        else:
            n = size - data  # n is the index of the mth node
            while node.next != None:  # noqa
                if count <= n:
                    node = node.next
                    count += 1
                else:
                    break
            return node.data


def question5(ll, m):
    return ll.findMthNode(m)


class Q5Test(unittest.TestCase):
    def test(self):
        ll = LinkedList()
        ll.insertNode(12)
        ll.insertNode(14)
        ll.insertNode(16)
        ll.insertNode(20)
        self.assertEqual(question5(ll, 2), 16)
        self.assertEqual(question5(ll, 4), 12)
        self.assertNotEqual(question5(ll, 3), 20)


if __name__ == '__main__':
    unittest.main()
