from __future__ import annotations
class Point:

    def __init__(self,x:int,y:int) -> None:
        self.x = x
        self.y = y

    def entfernung(self,point2:Point):
        xentf = self.x - point2.x
        yentf = self.y - point2.y
        return (xentf**2 + yentf**2)**0.5
