"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 0):
            return ''

        lens = min([len(s) for s in strs])
        rsu = '';   i = 0
        while(i < lens):
            if(len(set([s[i] for s in strs])) == 1):
                rsu = rsu + strs[0][i]
            else:
                break
            i+=1

        return rsu