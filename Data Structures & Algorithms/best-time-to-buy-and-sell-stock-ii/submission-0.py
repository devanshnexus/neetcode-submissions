class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def f(i, b):
            if i == len(prices): return 0
            if (i, b) in dp:
                return dp[(i, b)]
            res = f(i+1, b)
            if b:
                res = max(res, prices[i] + f(i + 1, False))
            else:
                res = max(res, -prices[i] + f(i + 1, True))
            dp[(i, b)] = res
            return res
        return f(0, False)