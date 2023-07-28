# 7-base_geometry.py

class BaseGeometry:
    """The base class of all Geometry"""

    def area(self):
        """Computes the area of a Geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates a value.

        Args:
            name(str): The name of the value
            value(int): The value to be stored
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

