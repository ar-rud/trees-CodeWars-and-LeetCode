"""
implementation of sorting binary tree by levels
"""
class Node:
    """node class"""
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node: Node) -> list[str]:
    """returns list of tree values sorted by levels"""
    if not node:
        return []

    queue = [node]
    res = []

    while queue:
        cur: Node = queue.pop(0)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
        res.append(cur.value)

    return res
