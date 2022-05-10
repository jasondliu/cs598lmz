import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100)) + ['READY\n']))).start()

#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
                j += 1
            prefix = prefix[:j]
        return prefix


# @lc code=end
