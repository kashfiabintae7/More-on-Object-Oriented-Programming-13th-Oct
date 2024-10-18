class Circle:
    PI = 3.1416
     
     
    def __init__(self, radius):
        self.radius = radius 
        
    
    def area(self):
       return (Circle.PI * self.radius * self.radius)    
           
    
    def perimeter(self):
        return (2 * Circle.PI * self.radius)
    
   
        
r = float(input("Enter the Radius of the Circle: "))

c1 = Circle(r)

print("Area of the Circle is: ", c1.area())
print("Perimeter of the Circle is: ", c1.perimeter())

r = float(input("Enter the radius of the Circle: "))
c2 = Circle(r)

print("Area of C1 Circle is: ", c2.area())
print("Perimeter of C1 Circle is: ", c2.perimeter())


