"""Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example:
    Input: root = [1,2,2,3,4,4,3]
Output: true """

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        def sym(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            return l.val == r.val and sym(l.left,r.right) and sym(l.right,r.left)
        return sym(root,root)
