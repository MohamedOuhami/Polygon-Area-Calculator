import math
class Rectangle:
  # Initializing the attributes ( width and height)
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  # Setting the width
  def set_width(self,width):
    self.width = width

  # Setting the height
  def set_height(self,height):
    self.height = height

  # Calculating the area of the rectangle
  def get_area(self):
    return self.width * self.height

  # Calculating the perimeter of the rectangle
  def get_perimeter(self):
    return 2*self.width + 2*self.height

  # Calculating the diagonal of the square
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) **.5

    
  def get_picture(self):
    # Checking if the dimensions are good

    if(self.width <= 50 and self.height <= 50):
      for i in range(self.height):
        for j in range(self.width):
            print('*',end ='')
        print("\n")
    else : 
        return None

    # Getting the amount of shapes inside the initial shape
  def get_amount_inside(self,Object):
    num_hor = math.floor(self.width / Object.width)
    num_ver = math.floor(self.height / Object.height)

    return num_hor * num_ver
        

class Square(Rectangle):
  
  def __init__(self,side):
    self.side = side
    self.width = side
    self.height = side

  def __str__(self):
    return f'Square(side={self.side})'
    
  # Setting the side
  def set_side(self,side):
    self.side = side
    self.width = side
    self.height = side
