class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums=[1,2,3,4]
        #output=[24,12,8,6]

        res=[1]*(len(nums)) #[1,1,1,1]
        prefix=1
        #left to right
        for i in range(len(nums)):
            res[i]=prefix 
            prefix = prefix * nums[i]

            #res=[1,1,2,6]
        postfix=1
        #right to left
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

            #res=[]
        return res            

        