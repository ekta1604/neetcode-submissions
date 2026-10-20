from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:   # skip same anchor
                continue
            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates on both sides
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1         # need larger sum → move left up
                else:
                    r -= 1         # need smaller sum → move right down
        return ans
