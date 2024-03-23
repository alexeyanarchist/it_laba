class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


    def length(self, second_point):
        return round(((second_point.x - self.x)**2 + (second_point.y - self.y)**2)**0.5, 2)
    
    

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
