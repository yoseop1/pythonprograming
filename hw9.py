class Point():
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x},{self.__y})')

    def set(self,x,y):
        self.__x = x
        self.__y = y

    def get(self):
        return (self.__x, self.__y)
    
    def get_x(self):
        return (self.__x)
    
    def get_y(self):
        return (self.__y)
    
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__lt = Point(x1, y1)
        self.__rb = Point(x2, y2)

    def show(self):
        print(f'좌측 꼭짓점 {self.__lt.get()}, 우측 꼭짓점 {self.__rb.get()}')

    def getWidth(self):
        ltx = self.__lt.get_x()
        rbx = self.__rb.get_x()
        width = rbx - ltx
        return width
   
    def getHeight(self):
        lty = self.__lt.get_y()
        rby = self.__rb.get_y()
        height = rby - lty
        return height

    def getArea(self):
        return self.getWidth() * self.getHeight()
    
    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
