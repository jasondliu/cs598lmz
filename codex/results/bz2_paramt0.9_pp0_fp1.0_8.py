from bz2 import BZ2Decompressor
BZ2Decompressor.extra_dealloc_bytes = 0
 
##############################################################################

class _PPDB:

    def _edit_distance(self, s1, s2):
        '''
        Levenshtein edit distance between sequences s1 and s2.
        '''

        m, n = len(s1), len(s2)
        if abs(m - n) > 10: # 10 is ad-hoc constant
            return 0.0
        
        d = array('i', [0]) * (n+1) # Initialize array to zero
        dp = array('i', [0] * (n+1))
        
        for i in range(m):
            dp[0] = i+1
            
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[j+1] = d[j]
                else:
                    dp[j+1] = min(d[j+1]+1, dp[j]+1, d[j]+1)
            
            for j in range
