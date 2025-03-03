nums = [1,2,4,0,3,5,7,6]

# 冒泡排序
# 从第一个元素开始，依次比较相邻的两个元素，如果前一个元素大于后一个元素，则交换两个元素的位置
# 一轮比较下来，最大的元素就会被交换到最后一个位置
# 重复上述操作，直到所有元素都排好序
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
# 稳定性：稳定

def buble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

print(buble_sort(nums))