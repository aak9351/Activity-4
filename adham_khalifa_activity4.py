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

    
    #######################
p = Polygon("triangle", [3.0,3.0,3.0])
def test_polygon_initilization():
    """Test function for initialized values"""
    assert p.get_name() is not None and p.get_side() is not None #Makes sures that none of the values are None



p1 = Polygon("square", [4.0,4.0,4.0])
def test_get_name():
    """Test function that checks for name"""
    getter_name = p1.get_name()
    if getter_name is None: #If getter returns a value the test passes
        assert False



p2 = Polygon("Pentagon",[1.0,1.0,1.0,1.0,1.0])
def test_get_side():
    """Test function that checks for side"""
    getter_side = p2.get_side()
    if getter_side is None:#If getter returns a value the test passes
        assert False


p3 = Polygon("square",[3.0,3.0,3.0,3.0])
def test_set_name():
    """Test function that checks the new name made meets the requirements"""
    new_name = "Triangle"
    p3.set_name(new_name)
    assert p3.get_name() == new_name #Checks new name is equal to the name returned from get function



p4 = Polygon("square",[4.0,4.0,4.0,4.0])
def test_set_side():
    """Test function "that checks the new sides made meet the requirements"""
    old_side = p4.get_side()
    new_side = [5.0,5.0,5.0,5.0]
    p4.set_side(new_side)
    assert len(p4.get_side()) == len(old_side) and type(p4.get_side()) == type(old_side) #Checks new sides is equal to the name returned from get function


def main():
    triangle = Polygon("Triangle", [3.0,3.0,3.0])#Class instance: Triangle
    square = Polygon("Square", [3.0,3.0,3.0,3.0])#Class instance: Square
    hexagon = Polygon("Hexagon",[3.0,3.0,3.0,3.0,3.0,3.0])#Class instance: Hexagon
    print(f"{triangle}\n{square}\n{hexagon}")
    print(f"{triangle.calculate_circumference()}\n{square.calculate_circumference()}\n{hexagon.calculate_circumference()}")
if __name__ == "__main__":
    main()