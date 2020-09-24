"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, newNode):
        if newNode < self.value:
            if not self.left:
                self.left = BSTNode(newNode)
            else:
                self.left.insert(newNode)
        else:
            if not self.right:
                self.right = BSTNode(newNode)
            else:
                self.right.insert(newNode)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self:
            return None
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return None

        if node.left:
            node.left.in_order_print(node.left)
            print(node.value)
        if node.right:
            node.right.in_order_print(node.right)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(5)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print(bst)
print("post order")
bst.post_order_dft()  

#     # Part 2 -----------------------

#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
#     def in_order_print(self):
#         if not self:
#             return None
#             #left -> root -> right
#         if self.left:
#             self.left.in_order_print()
#             print(self.value)
#         if self.right:
#             self.right.in_order_print()

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal
#     def bft_print(self):
#         if not self:
#             return None
#         # Define Deque
#         # Add self to deque
#         # iterate while there are item in the deque
#         # deqeue/pop frm deque and point to result and print
#         # add left and right child to deque

    


#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     import sys
#     sys.path.extend('queue')
#     from queue import Queue
#     def dft_print(self):
#         queue = Queue()
#         queue.put.(node)

#         while len(s) > 0:
#             current = s.pop()
#             print(current.value)
#             if current.left:
#                 s.append(current.left)

#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self):
#         if not self:
#             return
#         print(self.value)
#         if self.left:
#             self.left.pre_order_dft()
#         if self.right:
#             self.right.pre_order_dft()

#     def in_order_dft(self):
#         if not self:
#             return None

#     # Print Post-order recursive DFT
#     def post_order_dft(self):
#         if not self:
#             return
#         if self.left:
#             self.left.post_order_dft()

#         if self.right:
#             self.right.post_order_dft()
#         print(self.value)

# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(5)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
