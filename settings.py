import math

class Settings():
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)

  LIGHT = (253, 255, 226)
  LIGHT_BLUE = (131, 180, 255)
  LIGHT_NAVY = (90, 114, 160)
  DARK_BLUE = (26, 33, 48)
  def __init__(self) -> None:
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = self.LIGHT
    self.axis_color = self.DARK_BLUE
    self.font_color = self.DARK_BLUE

    self.circle_color = self.LIGHT_BLUE
    self.circle_width = 3
    self.circle_radius = 20

    self.point_color = self.LIGHT_NAVY
    self.first_angular =  math.pi / 2
    self.magnitude = self.circle_radius * 10
    self.frequency = math.pi / 1000