class Solution:
    def trap(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        left_max=right_max=0
        water=0
        while l<r:
            if h[l]<=h[r]:
                left_max=max(left_max,h[l])
                water=water+left_max-h[l]
                l+=1
            else:
                right_max=max(right_max,h[r])
                water=water+right_max-h[r]
                r=r-1
        return water
