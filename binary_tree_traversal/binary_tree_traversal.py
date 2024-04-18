"""
Implementation of tree traversal in
 - preorder
 - inorder
 - postorder

works recursively
"""

#      Node class is not implemented

#      The Node is suppossed to have the following properties:
#       - data
#       - left
#       - right

# Pre-order traversal
def pre_order(node):
    """preorder tree traversal implementation"""
    if not node:
        return []
    res = [node.data]
    if node.left:
        res.extend(pre_order(node.left))
    if node.right:
        res.extend(pre_order(node.right))

    return res

# In-order traversal
def in_order(node):
    """inorder tree traversal implementation"""
    if not node:
        return []
    res = []
    if node.left:
        res.extend(in_order(node.left))
    res.append(node.data)
    if node.right:
        res.extend(in_order(node.right))

    return res

# Post-order traversal
def post_order(node):
    """postorder tree traversal implementation"""
    if not node:
        return []
    res = []
    if node.left:
        res.extend(post_order(node.left))
    if node.right:
        res.extend(post_order(node.right))
    return res + [node.data]
