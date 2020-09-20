class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h


class Triangle(Shape):
    def area(self):
        return (self.width * self.height) / 2


class Rectangle(Shape):
    def area(self):
        return self.width * self.height


triangle = Triangle(w=10, h=12)
rectangle = Rectangle(w=10, h=12)
