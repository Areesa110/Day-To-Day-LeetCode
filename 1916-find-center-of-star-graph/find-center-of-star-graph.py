        # Time Complexity: O(1)
        # We only check the first two edges, regardless of input size.
        #
        # Space Complexity: O(1)
        # No extra data structure is created.
        # Extra memory stays constant as input size grows.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]