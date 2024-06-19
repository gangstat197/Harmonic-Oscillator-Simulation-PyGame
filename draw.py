import pygame

from settings import Settings

sim_settings = Settings()
class Draw():
    def __init__(self, screen):
        # Set the color & the font 
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = pygame.font.Font(None, 18)
        self.screen = screen

    def draw_axes(self):
        width, height = sim_settings.screen_width, sim_settings.screen_height
        center_x, center_y = width // 2, height // 2

        # X Axis
        pygame.draw.line(self.screen, sim_settings.DARK_BLUE, (0, center_y), (width, center_y), 2)
        # Y Axis
        pygame.draw.line(self.screen, sim_settings.DARK_BLUE, (center_x, 0), (center_x, height), 2)

        # Numbering
        for x in range(0, width, 50):
            if x != center_x:
                label = self.font.render(str((x - center_x) / 10), True, sim_settings.DARK_BLUE)
                self.screen.blit(label, (x, center_y + 5))

        for y in range(0, height, 50):
            if y != center_y:
                label = self.font.render(str((center_y - y) / 10), True, sim_settings.DARK_BLUE)
                self.screen.blit(label, (center_x + 5, y))

    def draw_circle(self):
        width, height = sim_settings.screen_width, sim_settings.screen_height
        center_x, center_y = width // 2, height // 2
        pygame.draw.circle(self.screen, sim_settings.circle_color, (center_x, center_y), sim_settings.circle_radius * 10, sim_settings.circle_width)

    def draw_point(self, position):
        width, height = sim_settings.screen_width, sim_settings.screen_height
        center_x, center_y = width // 2, height // 2
        pygame.draw.circle(self.screen, sim_settings.point_color, (center_x + position, center_y), radius = 5)
        

    def draw_point_around(self, position_x, position_y): 
        width, height = sim_settings.screen_width, sim_settings.screen_height
        center_x, center_y = width // 2, height // 2    
        pygame.draw.circle(self.screen, sim_settings.point_color, (center_x + position_x, center_y + position_y), radius = 5)

        pygame.draw.line(self.screen, sim_settings.axis_color, 
                         (center_x + position_x, center_y + position_y), 
                         (center_x, center_y))
        
        pygame.draw.line(self.screen, sim_settings.axis_color, 
                         (center_x + position_x, center_y + position_y), 
                         (center_x + position_x, center_y))

    def draw_info_box(self, position, elapsed_time):
        font = pygame.font.SysFont(None, 24)
        info_box_width = 200
        info_box_height = 100
        info_box_x = 10
        info_box_y = 10
        info_box_color = (255, 255, 255)  
        text_color = sim_settings.axis_color
        
        pygame.draw.rect(self.screen, info_box_color, (info_box_x, info_box_y, info_box_width, info_box_height))
        
        text_lines = [
            f"X: {position / 10:.2f}",
            f"First Angular: {sim_settings.first_angular:.2f}",
            f"Frequency: {sim_settings.frequency * 1000:.2f}",
            f"Magnitude: {sim_settings.magnitude / 10:.2f}"
        ]
        
        for i, line in enumerate(text_lines):
            text = font.render(line, True, text_color)
            self.screen.blit(text, (info_box_x + 10, info_box_y + 10 + i * 20))
