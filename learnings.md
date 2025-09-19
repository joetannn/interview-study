# Learnings from LC Problems

1. Two Sum 
* The solution here was to "save state" via a hashmap. When going through data, after the initial read on an index, the solution was known. Therefore, remove re-iteration by using a map to save and check for previous "solutions"

100. Max Depth
* Solution here was to use BFS for "leveling". Keep track of a level because everytime you do BFS, you go down a level, and therefore BFS can be used for "maximum depth problems". 
* For runtimes, the solution goes through every node - therefore O(N) for runtime. O(N) for space worst case, as we go through every node in the tree, and the bottom level of the tree is half the total size of the tree (O(N/2)) simplifies to O(N).

104. Min Depth
* Solution here was to track the level, as in problem 100. If you need to keep track of data specific to each node as you traverse a tree, use a tuple to store data in the queue with "tracking".
* Time and space for BFS is O(N), where N is the number of nodes.
* Also, `import sys` and use `sys.maxsize` for maximum size integer.