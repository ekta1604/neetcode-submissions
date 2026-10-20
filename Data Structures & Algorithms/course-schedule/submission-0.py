class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[]for i in range(numCourses)}
        for cur, pre in prerequisites:
            premap[cur].append(pre)
        visitset=set()
        def dfs(cur):
            if cur in visitset:
                return False
            if premap[cur]==[]:
                return True
            visitset.add(cur)
            for pre in premap[cur]:
                if not dfs(pre): return False
            visitset.remove(cur)
            premap[cur]=[]
            return True
        for cur in range(numCourses):
            if not dfs(cur): return False
        return True
            
