class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a_l, b_l=[],[]
        for i in range(len(img1)):
            for j in range(len(img2)):
                if img1[i][j]==1:
                    a_l.append((i,j))
                    
                if img2[i][j]==1:
                    b_l.append((i,j))
               
        d={}
        ans=0
        for a_x, a_y in a_l:
            for b_x, b_y in b_l:
                tr=(b_x - a_x, b_y-a_y)
                
                if tr in d:
                    d[tr]+=1
                else:
                    d[tr]=1
                    
                ans=max(ans,d[tr])
                
        return ans
                