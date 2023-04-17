class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies=max(candies)
        
        boolarr=[]
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= maxcandies:
                boolarr.append(True)
            else:
                boolarr.append(False)
                
        return boolarr