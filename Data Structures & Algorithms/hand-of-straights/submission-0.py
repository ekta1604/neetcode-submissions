class Solution:
    def isNStraightHand(self, hand: List[int], groupsize: int) -> bool:
        if len(hand)%groupsize:
            return False
        count={}
        for n in hand:
            count[n]=1+count.get(n,0)
        minheap=list(count.keys())
        heapq.heapify(minheap)
        while minheap:
            first=minheap[0]
            for i in range(first,first+groupsize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True
