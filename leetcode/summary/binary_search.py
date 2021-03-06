# -*- coding:utf-8 -*-
# binary search

def binary_search(nums,target):
    l,r = 0,len(nums)-1
    while l<=r:
        mid = l+((r-l)>>1)
        if nums[mid]>target:
            r = mid - 1
        elif nums[mid]<target:
            l = mid + 1
        else:
            return mid
    return -1

