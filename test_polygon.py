from polygon import Polygon
import pytest

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



p5 = Polygon("triangle", [2.0,2.0,2.0])
p6 = Polygon("triangle", [2.0,2.0,2.0])
def test_equal_object():
    """Test function that compares 2 class instances"""
    assert p5 == p6



p7 = Polygon("triangle", [2.0,2.0,2.0])
p8 = Polygon("triangle", [2.0,2.0,2.0])
def test_unequal_object():
    """Test function that checks for inequality of 2 class instances"""
    assert p7 != p8



p9 = Polygon("hexagon", [1.0,1.0,1.0,1.0,1.0,1.0])
def test_string():
    """Test function that checks the string provided of a class instance"""
    assert str(p9) == f"{p9.get_name()} with sides: {p9.get_side()}" #Checks that str of th eobject is equal to the example provided
     


p10 = Polygon("Pentagon",[4.0,4.0,4.0,4.0,4.0])
def test_circumference():
    """Test function that checks the circumference is provided correctly"""
    assert sum(p10.get_side()) == pytest.approx(p10.calculate_circumference()) #Approx checks equality of 2 numbers.

    