""""
给你一个整型数组
nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例
1：
输入：nums = [1, 2, 3]
输出：6
示例

2：
输入：nums = [1, 2, 3, 4]
输出：24
示例

3：
输入：nums = [-1, -2, -3]
输出：-6

提示：
3 <= nums.length <= 104
-1000 <= nums[i] <= 1000"""

class Solution:
    def maximumProduct(self, nums):
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        # 要么都大于0，三个最大的数相乘
        # 有正有负，一个正数和两个负数，或者最大三个数
        #都是负数，最大的三个数乘
        nums = sorted(nums)
        if nums[0] >=0 or nums[-1] <=0:
            return nums[-1] * nums[-2] * nums[-3]
        else:
            return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

if __name__ == '__main__':
    nums = Solution().maximumProduct([1, 2, 3,-4])
    print(nums)