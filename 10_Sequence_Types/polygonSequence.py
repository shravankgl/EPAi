from numbers import Number
import math
from RegularConvexPolygon import RegularConvexPolygon

class PolygonSequence:
    '''Creates a sequence of Regular Strictly Convex Polygons'''
    
    def __init__(self, edges:int, radius:Number)->None:
      '''Polygon sequence initializer with attributes edges and radius'''

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
        '''PolygonSequence representation'''
        return (f'A PolygonSequence from 3 to {self.edges} edges of radius {self.radius}')

    def __str__(self)->str:
        '''PolygonSequence string representation'''
        return (f'PolygonSequence: edges = (3 to {self.edges}), radius = {self.radius}')

    @property
    def edges(self)->int:
        '''Max edges of PolygonSequence'''
        return self.__edges

    @edges.setter
    def edges(self, edges:int)->None:
        '''set edges of PolygonSequence'''
        self.__validate_edges(edges)
        self.__edges = edges

    @property
    def radius(self)->Number:
        '''circumradius of polygon sequence'''
        return self.__radius

    @radius.setter
    def radius(self, radius:Number)->None:
        '''set circumradius of polygon sequence'''
        self.__validate_radius(radius)
        self.__radius = radius

    def __area_perimeter_ratio(self,edges:int)->Number:
      '''returns the area: perimeter ratio of polygon'''
      polygon = RegularConvexPolygon(edges,__ratio)
      return polygon.area/polygon.perimeter

    def max_efficiency(self)->str:
        '''returns the polygon with the highest area: perimeter ratio'''
        max_efficiency_value = __area_perimeter_ratio(3)
        max_efficiency_polygon = 3
        for i in range(4,__edges+1):
            curr_efficiency_value = __area_perimeter_ratio(i)
            if max_efficiency_value < curr_efficiency_value:
                max_efficiency_value = curr_efficiency_value
                max_efficiency_polygon = i
        return f"Max efficiency poygon is RegularConvexPolygon({max_efficiency_polygon},{__radius}) with area: perimeter ratio {max_efficiency_value}"

    def __getitem__(self, args)->RegularConvexPolygon:
        '''returns specified sequence'''    
        if isinstance(args, int):
            if args < 0:
                args = self.__edges - 2 + args
            if args < 0 or args >=(self.__edges - 2):
                    raise IndexError
            
            return RegularConvexPolygon(args + 3,self.__radius)
        else:
            start, stop, step = args.indices(self.__edges)
            return [RegularConvexPolygon(i+3, self.__radius) for i in range(start, stop, step)]
