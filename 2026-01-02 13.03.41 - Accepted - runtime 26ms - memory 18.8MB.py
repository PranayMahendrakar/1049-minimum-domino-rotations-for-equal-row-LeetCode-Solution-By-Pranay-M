class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        
        def check(target):
            # Count rotations to make all tops = target or all bottoms = target
            rotations_top = 0  # rotations to make tops all target
            rotations_bottom = 0  # rotations to make bottoms all target
            
            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    return float('inf')
                elif tops[i] != target:
                    rotations_top += 1
                elif bottoms[i] != target:
                    rotations_bottom += 1
            
            return min(rotations_top, rotations_bottom)
        
        # Only tops[0] or bottoms[0] can potentially be the answer
        result = min(check(tops[0]), check(bottoms[0]))
        
        return result if result != float('inf') else -1