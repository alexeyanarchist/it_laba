class Rectangle:

    def __init__(self, first_point, second_point):
        self.x1, self.y1 = first_point
        self.x2, self.y2 = second_point
        self.lenght = abs(self.x2 - self.x1)
        self.height = abs(self.y2 - self.y1)
        if self.y1 <= self.y2:
            self.y1, self.y2 = self.y2, self.y1
        if self.x1 >= self.x2:
            self.x1, self.x2 = self.x2, self.x1

    def perimeter(self):
        return round((self.lenght + self.height) * 2, 2)
    
    def area(self):
        return round(self.height * self.lenght, 2)

    def get_pos(self):
        return round(self.x1, 2), round(self.y1, 2)
    
    def get_size(self):
        return round(self.lenght, 2), round(self.height, 2)
    
    def move(self, dx, dy):
        self.x1, self.x2 = self.x1 + dx, self.x2 + dx
        self.y1, self.y2 = self.y1 + dy, self.y2 + dy
    
    def resize(self, wigth, height):
        self.x2, self.y2 = self.x1 + wigth, self.y1 - height
        self.lenght = abs(self.x2 - self.x1)
        self.height = abs(self.y2 - self.y1)
    
    def turn(self):
        self.center = round((self.x2 + self.x1) / 2, 2), round((self.y1 + self.y2) / 2, 2)
        print(self.center)
        self.x1, self.y1 = round(self.center[0] - self.height / 2, 2), round(self.center[1] + self.lenght / 2, 2)
        self.x2, self.y2 = round(self.center[0] + self.height / 2, 2), round(self.center[1] - self.lenght / 2, 2)
        self.lenght = abs(self.x2 - self.x1)
        self.height = abs(self.y2 - self.y1)
    
    def scale(self, scale):
        self.x1 *= scale
        self.x2 *= scale
        self.y1 *= scale
        self.y2 *= scale
        self.lenght = abs(self.x2 - self.x1)
        self.height = abs(self.y2 - self.y1)

rect = Rectangle((-1, -1), (-4, -6))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')