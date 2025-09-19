# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import sys
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = deque()
        queue.append((root, 1))
        minDepth = sys.maxsize

        while queue:
            for i in range(len(queue)):
                curr, depth = queue.popleft()
                if not curr.left and not curr.right:
                    minDepth = min(minDepth, depth)
                if curr.left:
                    queue.append((curr.left, depth + 1))
                if curr.right:
                    queue.append((curr.right, depth + 1))


        return minDepth