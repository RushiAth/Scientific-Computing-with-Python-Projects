class Rectangle:

  def __init__(self, w, h):
    self.width = w
    self.height = h

  def set_width(self, w):
    self.width = w

  def set_height(self, h):
    self.height = h

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    
    pic = ""

    for i in range(self.height):
      pic += '*' * self.width + '\n'

    return pic

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

  def __init__(self, sLen):
    self.width = sLen
    self.height = sLen

  def set_side(self, sLen):
    self.width = sLen
    self.height = sLen

  def set_width(self, sLen):
    self.width = sLen
    self.height = sLen

  def set_height(self, sLen):
    self.width = sLen
    self.height = sLen

  def __str__(self):
    return f'Square(side={self.width})'
