# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:03:12 2021

@author: yw347
"""

import pygame,sys
pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
while True:
    #updates canvas by drawing what should be drawn earlier on in the while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(120)