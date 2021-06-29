#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:15:38 2021

@author: apple
"""
#数组的度
def findShortestSubArray(nums):
    dict_memo = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in dict_memo:
            dict_memo[nums[i]].append(i)
        else:
            dict_memo[nums[i]] = [i]
    memory = [len(dict_memo[nums[0]]),dict_memo[nums[0]][-1] - dict_memo[nums[0]][0]]
    for each in dict_memo:
        if len(dict_memo[each]) == memory[0]:
            memory[1] = min(memory[1],dict_memo[each][-1] - dict_memo[each][0])
        elif len(dict_memo[each]) > memory[0]:
            memory[0] = len(dict_memo[each])
            memory[1] = dict_memo[each][-1] - dict_memo[each][0]
    return memory[1] + 1
#子域名访问计数
def subdomainVisits(cpdomains):
    dict_memo = {}
    result = []
    for each in cpdomains:
        each_list = each.split(' ')
        times = int(each_list[0])
        address = each_list[1]
        tokens = address.split('.')
        if len(tokens) == 2:
            memo = (tokens[1],tokens[0]+'.'+tokens[1])
        elif len(tokens) == 3:
            memo = (tokens[2],tokens[1]+'.'+ tokens[2],tokens[0] +'.'+tokens[1]+'.'+tokens[2])
        for element in memo:
            if element in dict_memo:
                dict_memo[element] += times
            else:
                dict_memo[element] = times
    for key,value in dict_memo.items():
        value = str(value)
        result.append(value + ' '+key)
    return result
#LRU缓存机制（参照了老师给的模版,python内部已经实现按时间顺序排列的key，value）
import collections
class LRUCache:
    def __init__(self, capacity):
        self.dict = collections.OrderedDict()
        self.remain = capacity
    def get(self, key):
        if key not in self.dict:
            return -1
        v = self.dict.pop(key)
        self.dict[key] = v
        return v
    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last = False)
        self.dict[key] = value
                