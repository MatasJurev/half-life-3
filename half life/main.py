import pygame
from time import sleep
from threading import Thread

pygame.init()
scrn = pygame.display.set_mode((600, 600))
pygame.display.set_caption('half life')

pic1 = pygame.image.load("hl1.jpg").convert()
pic2 = pygame.image.load("hl2.png").convert()
pic3 = pygame.image.load("hl3.jpg").convert()
pic4 = pygame.image.load("hl4.jpg").convert()


def game():
    while 1:
        scrn.blit(pic1, (0, 0))
        pygame.display.update()
        sleep(2)
        scrn.blit(pic2, (0, 0))
        pygame.display.update()
        sleep(2)
        scrn.blit(pic3, (0, 0))
        pygame.display.update()
        sleep(2)
        scrn.blit(pic4, (0, 0))
        pygame.display.update()
        sleep(2)


def music():
    pygame.mixer.init()
    pygame.mixer.music.load('hl.mp3')  # any mp3 file
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()


Thread(target=music).start()
Thread(target=game).start()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    else:
        continue
    break


pygame.quit()
