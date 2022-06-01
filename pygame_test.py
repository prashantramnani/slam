import pygame

(width, height) = (3000, 2000) # Dimension of the window

screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.flip()

running = True
while running:
	i = 2
	pygame.display.update()
	#for event in pygame.event.get():
  	#	i = 3
  #  if event.type == pygame.QUIT:
  #    running = False
  #    pygame.quit()
