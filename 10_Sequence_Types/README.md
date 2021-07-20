# Session 10 assignment of EPAi3.0
## Sequence Types

### Regular Convex Polygon
#### ** 1) Attributes
Regular convex polygon has 2 attributes 
a) edges: number of edges in the polygon
   datatype: int
b) radius: circumradius of the polygon
   datatype: any number (int, float, decimal)
   
#### ** 2) Validators
This class has 3 validators
##### 2.1) edge validator
a) validates if datatype is int else raises TypeError
b) validates value is greater than or equal to 3 else raises ValueError
```
    def __validate_edges(self, edges:int)->None:
        '''validates datatype and value of edges'''
        if type(edges) != int:
            raise TypeError(f"'edges' must be int not {edges.__class__.__name__} ")
        if edges < 3:
            raise ValueError(f"'edges' should be greater than or equal to 3")
```
##### 2.2) radius validator
a) validates if datatype is any number else raises TypeError
To do number validation number module is used
b) validates value is greater than or equal to 0 else raises ValueError
```
    def __validate_radius(self, radius:Number)->None:
        '''validates datatype and value of radius'''
        if not isinstance(5, Number):
            raise TypeError(f"'radius' must be a number(int/float/decimal) not {radius.__class__.__name__} ")
        if radius < 0:
            raise ValueError(f"'edges' should be greater than or equal to 3")
```
#### 2.3) object validator
Validates if object passed for comparision is of class RegularConvexPolygon else raises TypeError
```
    def __validate_polygon(self, other):
        '''validates data type of other object'''
        if not isinstance(other, RegularConvexPolygon):
            raise TypeError("RegularConvexPolygon cannot be compared with {other.__class__.__name__}")
```

### 3) Getters and Setters
private attributes __edges and __radius are wrapped with getters and setters
```
@property
    def edges(self)->int:
        '''edges of polygon'''
        return self.__edges

    @edges.setter
    def edges(self, edges:int)->None:
        '''set edges of polygon'''
        self.__validate_edges(edges)
        self.__edges = edges

    @property
    def radius(self)->Number:
        '''circumradius of polygon'''
        return self.__radius

    @radius.setter
    def radius(self, radius:Number)->None:
        '''set circumradius of polygon'''
        self.__validate_radius(radius)
        self.__radius = radius

```

### 4) Constructor/Initializer
```
    def __init__(self, edges:int, radius:Number)->None:
      '''Polygon initializer with attributes edges and radius'''

      self.edges = edges
      self.radius = radius
```

### 5) Properties
#### 5.1) Interior Angle
interiorAngle = (edges−2)* 180/ n
```
    @property
    def interior_angle(self)->float:
        '''calculate interior angle of polygon'''
        return (self.__edges - 2)*(180/self.__edges)
```
#### 5.2)
edgeLength,s = 2*R*sin⁡(π/n)
```
    @property
    def edge_length(self)->float:
        '''calculate edge length of polygon'''
        return (2 * self.__radius) * math.sin(math.pi/self.__edges)
```
#### 5.3) Apothem
apothem,a = R*cos⁡(π/n)
```
    @property
    def apothem(self)->float:
        '''calculate apothem of polygon'''
        return self.__radius * math.cos(math.pi/self.__edges)
```
#### 5.4) Perimeter
perimeter = n*s
```
   @property
    def perimeter(self)->float:
        '''calculate perimeter of polygon'''
        return self.__edges * self.edge_length
```
#### 5.1) Area
area = 0.5*n*s*a
```
    @property
    def area(self)->float:
        '''calculate area of polygon'''
        return (self.__edges * self.apothem*self.edge_length) / 2
```

### 6) Comparators
```
def __eq__(self,  other:'RegularConvexPolygon')->bool:
        '''check equality of two polygons'''
        self.__validate_polygon(other)
        return (self.__edges==other.__edges and self.__radius == other.__radius)

    def __gt__(self, other:'RegularConvexPolygon')->bool:
        '''check no of edges of current polygon is greater than no of edges of other polygons'''
        self.__validate_polygon(other)
        return self.__edges > other.__edges

    def __ge__(self, other:'RegularConvexPolygon')->bool:
        '''check no of edges of current polygon is greater than or equal to no of edges of other polygons'''
        self.__validate_polygon(other)
        return self.__edges >= other.__edges

    def __lt__(self, other:'RegularConvexPolygon')->bool:
        '''check no of edges of current polygon is less than no of edges of other polygons'''
        self.__validate_polygon(other)
        return self.__edges < other.__edges

    def __le__(self, other:'RegularConvexPolygon')->bool:
        '''check no of edges of current polygon is less than or equal to no of edges of other polygons'''
        self.__validate_polygon(other)
        return self.__edges <= other.__edges

```
