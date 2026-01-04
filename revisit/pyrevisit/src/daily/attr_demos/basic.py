import attrs.validators
from attrs import define, field


@define
class Empty:
    pass

e = Empty()

print(e)
print( e==Empty())
print(e is Empty())

@define
class Coordinate:
    x: int
    y: int


c1 = Coordinate(1, 2)
print(c1)
c2 = Coordinate(1, 2)
print(c1 == c2)
print(c1 is c2)

## data class

@define
class CoordinateData:
    x: int = field()
    y: int =field()
    _z:int = field(alias="_biz")

more_c1 = CoordinateData(1, 2,_biz="5")
print(more_c1)


"""
validator
"""
def x_smaller_than_y(instance, attribute, value):
    if value >= instance.y:
        raise ValueError("'x' has to be smaller than 'y'!")

@define
class DataWithValidation:
    x: int = field()
    y: int = field(validator=[attrs.validators.instance_of(int),x_smaller_than_y])
    @x.validator
    def check_x(self, attribute, value):
        print(attribute, value)
        if value < 10:
            raise ValueError("x must be greater than 10")

dv = DataWithValidation(x=12,y=-1)
print(dv.x)