class Rectangle:

    def __init__(self, first_point, second_point):
        self.x1, self.y1 = first_point
        self.x2, self.y2 = second_point
        self.lenght = abs(self.x2 - self.x1)
        self.height = abs(self.y2 - self.y1)

    def perimeter(self):
        return round((self.lenght + self.height) * 2, 2)
    
    def area(self):
        return round(self.height * self.lenght, 2)

rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())