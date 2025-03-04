"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""

# 解法1：暴力解法
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)

def sum_of_two_nums(nums, target):
    if len(nums) < 2:
        return []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

# 解法2：哈希表
# 时间复杂度：O(n)
# 空间复杂度：O(n)

def sum_of_two_nums(nums, target):
    if len(nums) < 2:
        return []
    num2idx = {}
    for i in range(len(nums)):
        if target - nums[i] in num2idx:
            return [num2idx[target-nums[i]], i]
        else:
            num2idx[nums[i]] = i
    return []

nums = [2,7,11,15]
target = 9
print(sum_of_two_nums(nums,target))

