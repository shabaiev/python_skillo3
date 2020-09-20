class Shape:

    def __init__(self, w, h):
        self.width = w
        self.height = h


class Triangle(Shape):
    def __init__(self, w, h):
        super().__init__(w, h)

    def area(self):
        return (self.width * self.height) / 2


class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__(w, h)

    def area(self):
        return self.width * self.height

        # (w * h) / 2
        # w * h


triangle = Triangle(w=10, h=12)
rectangle = Rectangle(w=10, h=12)

print(triangle.area())
print(rectangle.area())
