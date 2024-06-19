import sys
import os
import pygame

from settings import Settings
import sim_functions as sf
from draw import Draw


sim_settings = Settings()
bg_color = sim_settings.bg_color

def run_sim():
  pygame.init()
  screen = pygame.display.set_mode((sim_settings.screen_width, sim_settings.screen_height))
  screen.fill(bg_color)
  pygame.display.set_caption("Harmonic Oscillator Simulation")
  
  drawModule = Draw(screen)

  clock = pygame.time.Clock()
  while True: 
    sf.check_events()
    sf.update_screen(screen, drawModule, pygame.time.get_ticks())

run_sim()