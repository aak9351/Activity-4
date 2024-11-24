
class Polygon:
    __slots__ = ["__name", "__side"]
    
    def __init__(self, name, side):
        self.__name = name
        self.__side = side

    def get_name(self):
        """Returns the name of the class instance
        
           Arguments:
           1 - self: pointer for itself
        """
        return self.__name
    
    def set_name(self, name):
        """Sets the new name of the class instance
        
           Arguments:
           1 - self: pointer for itself
        """
        self.__name = name #New name of the shape

    def get_side(self):
        """Returns the sides of the class instance
        
           Arguments:
           1 - self: pointer for itself
        """
        return self.__side
    
    def set_side(self, side):
        """Sets the sides  of the class instance
        
           Arguments:
           1 - self: pointer for itself
        """
        self.__side = side #New values for side
    
    def __eq__(self,other):
        """Checks whether the class instances are equal

           Arguments:
           1 - self: pointer for itself
           2 - other: second class instance used for comparison
        """
        return isinstance(other, self.__class__) and self.__name == other.__name and self.__side == other.__side
    
    def __ne__(self,other):
        """Checks whether the class instances are unequal

           Arguments:
           1 - self: pointer for itself
           2 - other: second class instance used for comparison
           """
        return not self.__eq__(other)
        
        
    def __str__(self):
        """Default statement when printing a class insatnce
        
           Arguments:
           1 - self: pointer for itself
        """
        return f"{self.__name} with sides: {self.__side}"
    
    def calculate_circumference(self):
        """Calculates the circumference of shape given
        
           Arguments:
           1 - self: pointer for itself
        """
        sum = 0
        for value in self.__side: #Loop that continously adds all the elements ofa list
            sum = value + sum
        return sum




def main():
    triangle = Polygon("Triangle", [3.0,3.0,3.0])#Class instance: Triangle
    square = Polygon("Square", [3.0,3.0,3.0,3.0])#Class instance: Square
    hexagon = Polygon("Hexagon",[3.0,3.0,3.0,3.0,3.0,3.0])#Class instance: Hexagon
    print(f"{triangle}\n{square}\n{hexagon}")
    print(f"{triangle.calculate_circumference()}\n{square.calculate_circumference()}\n{hexagon.calculate_circumference()}")
if __name__ == "__main__":
    main()
        
