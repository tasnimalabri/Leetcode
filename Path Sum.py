"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values
along the path equals targetSum. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown."""

lass Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs_sum(curr=None, sumTill=0):
            if curr:
                sumTill += curr.val
                left = dfs_sum(curr.left, sumTill)
                right = False
                if not left:
                    right = dfs_sum(curr.right, sumTill)
                
                if curr.left == None and curr.right == None:
                    return sumTill == targetSum
                return left or right
            return False
        return dfs_sum(root)