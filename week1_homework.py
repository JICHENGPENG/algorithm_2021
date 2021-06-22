#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 13:39:43 2021

@author: apple
"""
#加一
def add_one(list_nums):
    if list_nums[-1] != 9:
        list_nums[-1] += 1
        return list_nums    
    n = len(list_nums)
    for i in range(n-1,-1,-1):
        if list_nums[i] != 9:
            list_nums[i] += 1
            break
        else:
            list_nums[i] = 0
    if list_nums[0] == 0:
        list_nums[0] = 1
        list_nums.append(0)           
    return list_nums
#合并两个有序链表
class ListNode():
    def __init__(self,val,next):
        self.val = val
        self.next = next        
def mergeTwoLists(l1, l2):  
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    current = ListNode(0)
    first = current
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            current.next = l1
            current = current.next
            l1 = l1.next
        else:
            current.next = l2
            current = current.next
            l2 = l2.next
        if l1 is None:
            current.next = l2
        elif l2 is None:
            current.next = l1
    return first.next
#和为k的子数组
def subarraySum(nums,k):
    n = len(nums)
    sum_list = [0] * n
    sum_list[0] = nums[0]
    for i in range(1,n):
        sum_list[i] = sum_list[i-1] + nums[i]
    result = 0
    dict_memo = {0:1}
    for i in range(n):
        if sum_list[i] - k in dict_memo:
            result += dict_memo[sum_list[i] - k]
        if sum_list[i] not in dict_memo:
            dict_memo[sum_list[i]] = 1
        else:
            dict_memo[sum_list[i]] += 1
    return result
#设计循环双端队列（看了官方题解，双指针）
class MyCircularDeque:
    def __init__(self,k):
        self.deque = [0] * k
        self.count = 0
        self.first = 0
        self.last = 0
        self.k = k
    def insertFront(self,value):
        if self.count == self.k:
            return False
        self.start = (self.start - 1) % self.k
        self.deque[self.start] = value
        self.count += 1
        return True
    def insertBack(self,value):
        if self.count == self.k:
            return False
        self.deque[self.last] = value
        self.last = (self.last + 1) % self.k        
        self.count += 1
        return True
    def deleteFront(self):
        if self.count == 0:
            return False
        self.start = (self.start + 1) % self.k        
        self.count -= 1
        return True
    def deleteBack(self):
        if self.count == 0:
            return False
        self.last = (self.last - 1) % self.k
        self.count -= 1
        return True
    def getFront(self):
        if self.count == 0:
            return -1
        return self.deque[self.start]
    def getBack(self):
        if self.count == 0:
            return -1
        return self.deque[self.last-1]
    def isEmpty(self):
        return not self.count
    def isFull(self):
        return self.count == self.k
      
        
        

        