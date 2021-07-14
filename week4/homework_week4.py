#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 16:20:09 2021

@author: apple
"""
#设计推特
from collections import defaultdict
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)
        self.tweets_time = defaultdict(list)
        self.time = 0
        self.follows = defaultdict(set)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].insert(0, tweetId)
        self.tweets_time[userId].append([self.time, tweetId])
        self.time+=1

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news = self.tweets_time[userId].copy()
        for f in self.follows[userId]:
            news+=self.tweets_time[f]
        if news: 
            news.sort(key=lambda x:x[0], reverse=True)
            return [t[1] for t in news][0:10]
        else: 
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follows[followerId]: 
            self.follows[followerId].remove(followeeId)


    
    def follow(self,followerId,followeeId):
        if followerId not in self.outMatrix:
            self.outMatrix[followerId] = {followerId,followeeId}
        else:
            self.outMatrix[followerId].add(followeeId)
   
    def unfollow(self,followerId,followeeId):
        if followerId in self.outMatrix and followeeId in self.outMatrix[followerId]:
            self.outMatrix[followerId].remove(followeeId)
            
#寻找旋转排序数组中最小值2
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = int((left + right) / 2)
        if nums[mid] > nums[right]: left = mid + 1
        elif nums[mid] < nums[right]: right = mid
        else: right = right - 1 
    return nums[left]