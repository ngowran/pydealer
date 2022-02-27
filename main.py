import pygame
import random

# sets the game window's demntions and the black background
WIDTH = 800
HEIGHT = 600
BACKGROUND = (220, 20, 60)

# a test call to view an object in the game window
class Test_obj(object):
	def __init__(self):
		# .image is used to load in the png
		self.image = pygame.image.load("assets/cards-png/10_of_clubs.png")
		
		# rect gets the coodrinates of the object
		self.rect = self.image.get_rect()

def main():
	# init starts the screen and the clock
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()
	test_obj = Test_obj()

	while True:
		screen.fill(BACKGROUND)
		# blit moves all the pixels of our game image into the screen
		screen.blit(test_obj.image, test_obj.rect)
		# flip updates the screen
		pygame.display.flip()
		# the game redraws the game screen 60 times per sec
		clock.tick(60)

if __name__=="__main__":
	main()