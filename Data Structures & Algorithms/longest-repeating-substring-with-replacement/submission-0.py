class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen={}
        best=0
        l=0
        for r in range(len(s)):
            seen[s[r]]=1+seen.get(s[r],0)
            while (r-l+1)-max(seen.values())>k:
                seen[s[l]]-=1
                l+=1
            best=max(best,r-l+1)
        return best
        
    