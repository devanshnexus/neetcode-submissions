class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for n in nums: cnt[n] = 1 + cnt.get(n, 0)
        arr = []
        for n, c in cnt.items():
            arr.append([c, n])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res