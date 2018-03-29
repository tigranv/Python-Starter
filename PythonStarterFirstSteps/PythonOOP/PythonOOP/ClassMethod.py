class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    
    def __repr__(self):
        return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)



class Circle:
    def __init__(self, radius):
        self.radius = radius 
        
    def __repr__(self):
        return "Circle(%.1f)" % (self.radius)

    @classmethod
    def from_rectangle(cls, rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)

def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)

    first_circle = Circle(1)
    print(first_circle)

    second_circle = Circle.from_rectangle(rectangle)
    print(second_circle)

    second_circle2 = Circle.from_rectangle(rectangle)
    


main()

