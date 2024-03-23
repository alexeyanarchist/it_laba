class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def length(self, snd_point):
        return round(((snd_point.x - self.x)**2 + (snd_point.y - self.y)**2)**0.5, 2)

fst_point = Point(2, -7)
snd_point = Point(7, 9)
print(fst_point.length(snd_point))
print(snd_point.length(fst_point))
