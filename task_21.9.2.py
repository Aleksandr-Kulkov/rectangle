class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height

rect_1 = Rectangle(5, 10)
print(rect_1.get_area())
