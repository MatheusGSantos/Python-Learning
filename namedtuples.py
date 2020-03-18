"""
    Namedtuples: same as a tuple, but with tags, kinda.
"""

from collections import namedtuple

# example
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(255,245,235)

print(color.red) # or color[0]
print(color.green) # or color[1]
print(color.blue) # or color[2]

# example 2
Point = namedtuple('Point', ['x', 'y'])
point = Point(10,7)
print(point.x)
print(point.y)