'''
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.
Return the maximum sum of values that you can receive by attending events.

Example 1:
Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:
Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
Example 3:
Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
'''

import bisect
import functools
import math

class Solution:
  def maxValue(self, events: list[list[int]], k: int) -> int:
    e = sorted(events)

    @functools.lru_cache(None)
    def dp(i, k):
      if k == 0 or i == len(e):
        return 0

      # Binary search events to find the first index j s.t. e[j][0] > e[i][1]
      j = bisect.bisect(e, [e[i][1], math.inf, math.inf], i + 1)
      return max(dp(i + 1, k), e[i][2] + dp(j, k - 1))

    return dp(0, k)