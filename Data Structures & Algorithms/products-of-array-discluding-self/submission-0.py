class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, zc = 1, 0
        for n in nums:
            if n: p *= n
            else: zc += 1
        if zc > 1 : return [0] * len(nums)
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zc : res[i] = 0 if c else p
            else: res[i] = p // c
        return res