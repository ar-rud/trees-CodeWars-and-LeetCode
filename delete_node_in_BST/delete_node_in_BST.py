"""
Implementation of delete node in BTS function
"""

# The problem can be subdivided into two smaller:
#  1. find the node if any
#  2. delete it and replace with left child if any
# then dive to the lowest right child in that left subtree
# and make right subtree its rightchild

# corner case: the node to delete is root node

# Definition for a binary tree node.

class TreeNode:
    """treenode class"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root: TreeNode, key: int) -> TreeNode:
    """deletes tree node"""
    if not root:
        return root
    cur: TreeNode = root


    #handling corner case: key = value
    if root.val == key:
        if root.left:
            left_subtree = root.left
            cur0: TreeNode = left_subtree
            while cur0.right:
                cur0 = cur0.right
            cur0.right = root.right
            return left_subtree
        return root.right

    parent: TreeNode = root

    while cur.val != key:
        if cur.val < key:
            parent = cur
            cur = cur.right
        elif cur.val > key:
            parent = cur
            cur = cur.left
        #handling corner case: node was not found
        if not cur:
            return root
    #restructuring value(that will be deleted)'s children
    if cur.left:
        left_subtree = cur.left
        cur0: TreeNode = left_subtree
        while cur0.right:
            cur0 = cur0.right
        cur0.right = cur.right
    else:
        left_subtree = cur.right

    #deleting value and attaching to its parent its restructured children
    if parent.left and parent.left.val == cur.val:
        parent.left = left_subtree
    elif parent.right and parent.right.val == cur.val:
        parent.right = left_subtree
    return root
