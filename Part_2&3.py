import pytest
class Polygon:
    '''Creating functions that test for equality or inequality between two
    polygons and another function to print a sentence with a specific format
    with only certain values changing depending on the polygon'''
    def __eq__(self, other):   #checks between itself and another object given as paraameter 
        if self.name == other.name and self.side == other.side:  #both name and no. of sides should be same
            return True
    def __neq__(self, other):
        if self.name != other.name or self.side != other.side:  #Either name or no. of sides shoud be different
            return True
    def __str__(self):
        return f'{self.name} with sides: {self.side}'  #Prints a sentence having given layout but different values.
    