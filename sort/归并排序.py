nums = [1,2,4,0,3,5,7,6]

# 归并排序
# 将数组分为两部分，分别对两部分进行排序
# 将两部分合并
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)
# 稳定性：稳定

def merge_sort(nums):
    if len(nums) <2:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    l, r = 0, 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res.extend(left[l:])
    res.extend(right[r:])
    return res

print(merge_sort(nums))