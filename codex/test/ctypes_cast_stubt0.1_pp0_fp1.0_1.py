import ctypes
ctypes.cast(0, ctypes.py_object)

#import sys
#sys.setrecursionlimit(100000)

#import thread
#thread.stack_size(67108864)
#sys.setrecursionlimit(2 ** 20)

#import sys
#print sys.getdefaultencoding()
#reload(sys)
#sys.setdefaultencoding('utf-8')
#print sys.getdefaultencoding()

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum


