from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 1:
            return [0]

        ret = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ret[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return ret
    
if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([30,40,50,60]))
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))


        