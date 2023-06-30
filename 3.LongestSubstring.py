'''
Given a string s, find the length of the longest substring without repeating characters.
Substring = A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        unique_list = []
        result = 0
        for i in range (n):
            for j in range (i, n):
                if (s[j] in unique_list):
                    unique_list.clear()
                    break
                else:
                    unique_list.append(s[j])
                    if(result<j-i+1):
                        result = j-i+1
        return result