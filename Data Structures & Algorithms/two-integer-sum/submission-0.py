class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, x in enumerate(nums):
            need=target-x
            if need in seen:
                a,b=seen[need],i
                return[a,b] if a<b else [b,a]
            seen[x]=i
        return []

        