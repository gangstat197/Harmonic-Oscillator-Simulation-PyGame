import sys 

import pygame 

import math
from settings import Settings

sim_settings = Settings()
def check_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

def update_screen(screen, drawModule, elapsed_time):
  screen.fill(sim_settings.bg_color)
  drawModule.draw_axes()
  drawModule.draw_circle()

  position = calculate_point_pos(elapsed_time)

  position_x, position_y = calculate_around_point(elapsed_time)

  drawModule.draw_point(position)
  drawModule.draw_point_around(position_x, position_y)

  drawModule.draw_info_box(position, elapsed_time)
  pygame.display.flip()

def calculate_point_pos(elapsed_time) :
  position = sim_settings.magnitude * math.cos(sim_settings.frequency * elapsed_time + sim_settings.first_angular)
  # print(position)
  return position

def calculate_around_point(elapsed_time) :
  angle = sim_settings.frequency * elapsed_time + sim_settings.first_angular
  position_x = sim_settings.magnitude * math.cos(angle)
  position_y = sim_settings.magnitude * math.sin(angle)
  return position_x, position_y