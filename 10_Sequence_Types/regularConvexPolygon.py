from numbers import Number
import math

class RegularConvexPolygon:
    '''A Regular Strictly Convex Polygon'''
    
    def __init__(self, edges:int, radius:Number)->None:
      '''Polygon initializer with attributes edges and radius'''

      self.edges = edges
      self.radius = radius

    def __validate_edges(self, edges:int)->None:
        '''validates datatype and value of edges'''
        if type(edges) != int:
            raise TypeError(f"'edges' must be int not {edges.__class__.__name__} ")
        if edges < 3:
            raise ValueError(f"'edges' should be greater than or equal to 3")

    def __validate_radius(self, radius:Number)->None:
        '''validates datatype and value of radius'''
        if not isinstance(5, Number):
            raise TypeError(f"'radius' must be a number(int/float/decimal) not {radius.__class__.__name__} ")
        if radius < 0:
            raise ValueError(f"'edges' should be greater than or equal to 3")

    def __repr__(self)->str:
        '''RegularPoly representation'''
        return (f'A Regular Strictly Convex Polygon of {self.edges} edges and radius {self.radius}')

    def __str__(self)->str:
        '''RegularPoly string representation'''
        return (f'Regular Strictly Convex Polygon: edges = {self.edges}, radius = {self.radius}')

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

    @property
    def interior_angle(self)->float:
        '''calculate interior angle of polygon'''
        return (self.__edges - 2)*(180/self.__edges)

    @property
    def edge_length(self)->float:
        '''calculate edge length of polygon'''
        return (2 * self.__radius) * math.sin(math.pi/self.__edges)

    @property
    def apothem(self)->float:
        '''calculate apothem of polygon'''
        return self.__radius * math.cos(math.pi/self.__edges)

    @property
    def area(self)->float:
        '''calculate area of polygon'''
        return (self.__edges * self.apothem*self.edge_length) / 2

    @property
    def perimeter(self)->float:
        '''calculate perimeter of polygon'''
        return self.__edges * self.edge_length

    def __validate_polygon(self, other):
        '''validates data type of other object'''
        if not isinstance(other, RegularConvexPolygon):
            raise TypeError("RegularConvexPolygon cannot be compared with {other.__class__.__name__}")

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
