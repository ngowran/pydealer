import pygame
import sys

# sets the game window's demntions
WIDTH = 800
HEIGHT = 600
BACKGROUND = (0, 0, 0)

# a test call to view an object in the game window
class Test_obj:
	def __init__(self):
		
		self.image = pygame.image.load("small_tennis.png")
		self.rect = self.image.get_rect()

def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()

	while True:
		screen.fill(BACKGROUND)
		clock.tick(60)

if __name__=="__main__":
	main()