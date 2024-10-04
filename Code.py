class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        t = []
        s1 = 0
        for x in range(len(skill)//2):
            y = 0-x-1
            s = skill[x] + skill[y]
            if((x!=0) and (s != s1)):
                return -1
            else:
                s1 = s 
            t.append([skill[x],skill[y]])
        r = [x[0]*x[1] for x in t]
        return sum(r)

