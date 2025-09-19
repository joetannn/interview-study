
# iterative implementation of breath first search.

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.left, self.right = None
        self.val = val


def bfs(root):
    queue = deque()

    if root:
        queue.append(root)

    while len(queue) > 0:
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)



            