import pygame

red = (255, 0, 0)
white= (255, 255, 255)
blue =(0, 0 , 255)

pygame.init()
screen = pygame.display.set_mode((640,480))

pygame.draw.line(screen, blue, (60, 60 ), (120,60), 4)
pygame.draw.ellipse(screen, red, (300, 250, 40,80),1)

pygame.draw.rect(screen, red, (50,50,100,25) )
pygame.draw.polygon(screen, white,((146, 0), (291, 106), (236, 277), (56,277), (0,106)))

pygame.draw.circle(screen, blue,(200,50) , 35)
pygame.draw.polygon(screen, white,((250,100),(300,0),(350,50)))
pygame.draw.arc(screen,blue,(400,10,150,100),0,3.14)
pygame.display.flip()