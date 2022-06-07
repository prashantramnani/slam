#!/usr/local/bin/python3

import pygame


class Surface:
    def __init__(self, W, H):
        pygame.init()
        self.screen = pygame.display
        self.surface = self.screen.set_mode([W, H])

    def paint(self, frame):
        surf = pygame.surfarray.make_surface(frame)
        self.surface.blit(surf, (0,0))
        self.screen.update()

 
