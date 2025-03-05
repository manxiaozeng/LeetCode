"""给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。

示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。

提示：
3 <= nums.length <= 3000
-105 <= nums[i] <= 105"""

def sums_of_two_nums(nums, target):
    left = 0
    right = len(nums) - 1
    res = []
    while left < right:
        if nums[left] + nums[right]<-target:
            left += 1
        elif nums[left] + nums[right] >-target:
            right -= 1
        else:
            cur_res = sorted([target, nums[left], nums[right]])
            if cur_res not in res:
                res.append(cur_res)
            left += 1
            right -= 1
    return res

# 三数之和
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)

def sums_of_three_nums(nums):
    if len(nums) <3:
        return []
    if len(nums) == 3:
        if sum(nums) == 0:
            return nums
        else:
            return []
    nums = sorted(nums)
    res = []
    for i in range(len(nums)-2):
        if i >0 and nums[i] == nums[i-1]:
            continue
        num_res = sums_of_two_nums(nums[i+1:], nums[i])
        if len(num_res)>0:
            res = res + num_res
    return res

print(sums_of_three_nums([-1,0,1,2,-1,-4]))

