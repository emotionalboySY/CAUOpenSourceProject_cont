import sys
import pygame
import time
from botplay import botPlay

from constant import WIDTH, HEIGHT, IsExit, RestartGameSingle, RestartGameDual
from dualplay import dualPlay
from singleplay import singlePlay
from menu import Menu

pygame.init()

speed = [2, 2]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

start = True

# Create Menu
menu = Menu(pygame, screen)

while True:
    if RestartGameSingle:
        if not IsExit:
            RestartGameSingle, IsExit = singlePlay(pygame, screen, menu, False)
    if RestartGameDual:
        RestartGameDual = dualPlay(pygame, screen, menu)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                RestartGameSingle, IsExit = singlePlay(pygame, screen, menu, False)
            if event.key == pygame.K_d: ##! Dual player Mode
                RestartGameDual = dualPlay(pygame, screen, menu)
            if event.key == pygame.K_l:
                RestartGameSingle, IsExit = singlePlay(pygame, screen, menu, True)
            if event.key == pygame.K_r:
                menu.displayRanking(pygame)
            if event.key == pygame.K_b:
                RestartBot = botPlay(pygame, screen, menu)
            if event.key == pygame.K_e or event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()
    menu.displayStartMenu()
