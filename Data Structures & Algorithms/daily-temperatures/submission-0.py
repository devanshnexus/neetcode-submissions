class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        res = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and t[j] <= t[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]
            if j < n:
                res[i] = j - i
        return res