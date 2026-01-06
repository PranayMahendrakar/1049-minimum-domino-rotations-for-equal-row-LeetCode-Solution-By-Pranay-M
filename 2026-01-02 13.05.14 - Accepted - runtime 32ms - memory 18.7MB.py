class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(target):
            # Try to make all tops = target
            rot_top = 0
            rot_bottom = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return float('inf')
                if tops[i] != target:
                    rot_top += 1
                if bottoms[i] != target:
                    rot_bottom += 1
            return min(rot_top, rot_bottom)
        
        # Only need to check tops[0] and bottoms[0] as candidates
        result = min(check(tops[0]), check(bottoms[0]))
        return result if result != float('inf') else -1