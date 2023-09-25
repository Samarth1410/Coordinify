import math 
class Coordinate:
    def __init__ (self,x_axis,y_axis):
        self.xaxis = x_axis
        self.yaxis = y_axis
    
    def __str__(self):
        return "X = {} and Y = {}".format(self.xaxis, self.yaxis)
    
    
    # Basic operations such as addition, substraction, multiplication & division of the coordinates
    
    def __add__(self, other):
        temp_x = self.xaxis + other.xaxis
        temp_y = self.yaxis + other.yaxis
        return Coordinate(temp_x,temp_y)
    
    def __sub__(self,other):
        temp_x = self.xaxis - other.xaxis
        temp_y = self.yaxis - other.yaxis
        return Coordinate(temp_x,temp_y)
        
    def __mul__(self,other):
        temp_x = self.xaxis * other.xaxis
        temp_y = self.yaxis * other.yaxis
        return Coordinate(temp_x,temp_y)
        
    def __truediv__(self,other):
        temp_x = self.xaxis / other.xaxis
        temp_y = self.yaxis / other.yaxis
        return Coordinate(temp_x,temp_y)
    
    #Distance between two coordinates
    def distance(self,other):
        temp_x = abs(self.xaxis - other.xaxis)**2
        temp_y = abs(self.yaxis / other.yaxis)**2
        return Coordinate(temp_x,temp_y)
        
    #Midpoint between two coordinates
    def midpoint(self,other):
        temp_x = abs(self.xaxis - other.xaxis)**2 / 2
        temp_y = abs(self.yaxis / other.yaxis)**2 / 2
        return Coordinate(temp_x,temp_y)
    
    #Slope between two points
    def slope(self,other):
        return (other.yaxis - self.yaxis)/(other.xaxis - self.xaxis)
        
    #Angle with x axis
    def angle_with_x_axis(self,other):
        degree = math.degrees(math.tan((other.yaxis - self.yaxis)/(other.xaxis - self.xaxis)))
        return degree
        
    #Angle with y axis
    def angle_with_y_axis(self,other):
        return 90 - self.angle_with_x_axis(other)
    
    @staticmethod # Method that belongs to a class but does not need an instance of that class for calling it from the code
    # Angle between two lines given their slopes
    def angle_between_slopes(slope1,slope2):
        temp = abs((slope2-slope1)/(1+slope1*slope2))
        return math.degrees(math.tan(temp))
    
    # Calculates the area of a triangle formed by three coordinates
    def triangle_area(self,other2,other3):
        
        return abs(self.xaxis*(other2.yaxis - other3.yaxis) + 
        other2.xaxis*(other3.yaxis - self.yaxis) + 
        other3.xaxis*(self.yaxis - other2.yaxis)) * 0.5
    
    #Scale the coordinates
    def scale(self,factor):
        return Coordinate(self.xaxis*factor,self.yaxis*factor)
    
    #Reflection of point in a line
    def reflect(self, line_start, line_end):
        # Calculate the slope and y-intercept of the line
        slope = line_start.slope(line_end)
        intercept = line_start.yaxis - slope * line_start.xaxis

        # Calculate the slope and y-intercept of the perpendicular bisector passing through
        # the given point
        perpendicular_slope = -1 / slope
        perpendicular_intercept = self.yaxis - perpendicular_slope * self.xaxis
        intersection_x = (perpendicular_intercept - intercept) / \
            (slope - perpendicular_slope)
        intersection_y = slope * intersection_x + intercept
        reflected_x = round(2 * intersection_x - self.xaxis, 3)
        reflected_y = round(2 * intersection_y - self.yaxis, 3)
        return Coordinate(reflected_x, reflected_y)
        
    # Find the distance between a point and a line
    def distance_to_line(self, line_start, line_end):
        """
        Computes the perpendicular distance from the current point to the line
        defined by two other points.

        Args:
            line_start (Coordinate): The starting point of the line.
            line_end (Coordinate): The ending point of the line.

        Returns:
            float: The distance from the current point to the line.
        """
        numerator = abs((line_end.yaxis - line_start.yaxis) * self.xaxis - (line_end.xaxis - line_start.xaxis)
                        * self.yaxis + line_end.xaxis * line_start.yaxis - line_end.yaxis * line_start.xaxis)
        denominator = ((line_end.yaxis - line_start.yaxis) ** 2 +
                       (line_end.xaxis - line_start.xaxis) ** 2) ** 0.5
        return round((numerator / denominator), 3)
        
    # Find the equation of a line
    def line_equation(self, point2):
        """
        Computes the equation of the line passing through two points.

        Args:
            point2 (Coordinate): The second point on the line.

        Returns:
            str: A string representation of the equation of the line.
        """
        slope = round(self.slope(point2), 3)
        intercept = round(self.yaxis - slope * self.xaxis, 3)
        return f"y = {slope}x + {intercept}"

        
        
a = Coordinate(10,20)
b = Coordinate(20,12)
c = Coordinate(13,40)
print(a)
print("A+B={}".format(a+b))
print("A-B={}".format(a-b))
print("A*B={}".format(a*b))
print("A/B={}".format(a/b))
        
print("Distance a and b = {}".format(a.distance(c)))
print("midpoint between a and b = {}".format(a.midpoint(b)))
print("Slope between a and b = {}".format(a.slope(b)))
print("angle_with_x_axis between a and b = {}".format(a.angle_with_x_axis(b)))
print("angle_with_y_axis between a and b = {}".format(a.angle_with_y_axis(b)))

print("Angle between slopes = {}".format(a.angle_between_slopes(20,12)))
print("triangle_area = {}".format(a.triangle_area(b,c)))
print("scale = {}".format(a.scale(80)))
print("Reflect = {}".format(a.reflect(b,c)))
print("Distance to line = {}".format(a.distance_to_line(b,c)))        
print("{}".format(a.line_equation(b)))
        
        
        