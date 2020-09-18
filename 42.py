# 42. Trapping Rain Water
# Hard

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        m = len(height)
        if m == 0:
            return 0

        stack = []
        res = 0
        stack.append(0)
        for i in range(1, m):
            top = stack[-1]
            if height[i] <= height[top]:
                stack.append(i)
            else:
                while stack and height[top] < height[i]:
                    stack.pop()
                    if not stack:
                        break
                    next_top = stack[-1]
                    dis = i - next_top - 1
                    h = min(height[i], height[next_top]) - height[top]
                    res += dis*h
                    top = next_top
                stack.append(i)

        return res


S = Solution()

case1 = [0,1,0,2,1,0,1,3,2,1,2,1]
res1 = S.trap(case1)
print('res1:', res1)

case2 = [4,2,3]
res2 = S.trap(case2)
print('res2:', res2)

case3 = [5,4,1,2]
res3 = S.trap(case3)
print('res3:', res3)
