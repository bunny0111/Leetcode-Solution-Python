'''
2272. Substring With Largest Variance
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.
Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.

Example 2:
Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.
'''
import string
class Solution:
  def largestVariance(self, s: str) -> int:
    # A := the w// higher freq
    # B := the w// lower freq
    def kadane(a: str, b: str) -> int:
      ans = 0
      countA = 0
      countB = 0
      canExtendPrevB = False

      for c in s:
        if c != a and c != b:
          continue
        if c == a:
          countA += 1
        else:
          countB += 1
        if countB > 0:
          # An interval should contain at least one b
          ans = max(ans, countA - countB)
        elif countB == 0 and canExtendPrevB:
          # Edge case: consider previous b
          ans = max(ans, countA - 1)

        # Reset if # Of b > # Of a
        if countB > countA:
          countA = 0
          countB = 0
          canExtendPrevB = True

      return ans

    return max(kadane(c1, c2)
               for c1 in string.ascii_lowercase
               for c2 in string.ascii_lowercase
               if c1 != c2)