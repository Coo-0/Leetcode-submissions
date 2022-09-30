class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # make the height negative inorder to get the maximum height for blds starting at the same position while sorting
            changes = [[start, -height, end] for start, end, height in buildings]
            # add the ending positions separetly to know when each buildng ends, height and start ing position won't matter here 
            changes += [[end, 0, 0] for start, end, height in buildings]
            # sort first by starting position and if there's a tie by height
            changes.sort()

            res = [[0, 0]]
            # inf for the endig position it's just a place holder
            heap = [(0, float('inf'))]

            for start, height, end in changes:
                # if this is and end for the tallest bld, then we need to pop it
                while heap[0][1] <= start:
                    heappop(heap)

                # if this is an ending list, then the height would be 0 so not pushed 
                if height:
                    heappush(heap, (height, end))

                # if there is a change in the maximum height, we need to append to the res
                if res[-1][1] != -heap[0][0]:
                    res.append([start, -heap[0][0]])

            # excluding the [0, 0]
            return res[1:]