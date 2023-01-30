class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        e1 = (ax2-ax1)*(ay2-ay1)
        e2 = (bx2-bx1)*(by2-by1)
        xo = max(min(ax2,bx2)-max(ax1,bx1), 0)
        yo = max(min(ay2,by2)-max(ay1,by1), 0)
        return (e1+e2)-(xo*yo)

