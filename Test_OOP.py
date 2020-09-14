class Point:

    def __init__(self, dx = 0, dy = 0):
        self.x = dx
        self.y = dy

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def set_location(self, dx, dy):
        self.x = dx
        self.y = dy

    def distance(self, otherPoint):
        if type(otherPoint) != type(self):
            raise TypeError
        else:
            return ((self.x - otherPoint.x)**2  + (self.y -otherPoint.y)**2 )**0.5
            
    def originDistance(self):
        origin = myPoint()
        return self.distance(origin)
        
    def __repr__(self):
        return "x: {}, y:{}".format(self.x, self.y)



