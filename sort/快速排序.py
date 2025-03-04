nums = [1,2,4,0,3,5,7,6]

# 快速排序
# 从数列中挑出一个元素，称为"基准"（pivot）
# 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆放在基准后面
# 在这个分区退出之后，该基准就处于数列的中间位置
# 递归地把小于基准值元素的子数列和大于基准值元素的子数列排序
# 时间复杂度：O(nlogn)
# 空间复杂度：O(logn)
# 稳定性：不稳定

def quick_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums)//2
    left = [num for num in nums if num<nums[mid]]
    right = [num for num in nums if num>nums[mid]]
    cur = [num for num in nums if num==nums[mid]]
    return quick_sort(left) + cur + quick_sort(right)

print(quick_sort(nums))