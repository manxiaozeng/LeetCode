nums = [1,2,4,0,3,5,7,6]

# 插入排序
# 从第一个元素开始，该元素可以认为已经被排序
# 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 如果该元素（已排序）大于新元素，将该元素移到下一位置
# 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 将新元素插入到该位置后
# 重复步骤2~5
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
# 稳定性：稳定

def insert_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i-1
        while j >= 0:
            if nums[j] > tmp:
                nums[j+1] = nums[j]
                j -= 1
            else:
                break
        nums[j+1] = tmp
    return nums

print(insert_sort(nums))

