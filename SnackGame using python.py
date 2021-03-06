import pygame
import time
import random

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width = 1200
display_hight = 600
gameDisplay = pygame.display.set_mode((display_width,display_hight))
pygame.display.set_caption("#Snake Game Created By Supto")
#pygame.display.flip()

clock = pygame.time.Clock()
block_size = 10
FPS = 20


font = pygame.font.SysFont(None, 25)
def snake(block_size,snakeList):
    for XnY in snakeList:
       pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_hight/2])
    
def gameLoop():
    gameExit = False
    gameOver = False
    lead_x =display_width/2
    lead_y = display_hight/2
    
    lead_x_change = 0
    lead_y_change = 0
    
    snakeList = []
    snakeLength = 1
    #point = 0
    randAppleX =round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_hight-block_size )/10.0)*10.0
    
    while not gameExit:
       while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over! U Looser!! Press C to play again or press Q to Quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                         gameExit = True
                         gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

           
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   lead_x_change = -block_size
                   lead_y_change = 0
                   
                elif event.key == pygame.K_RIGHT:
                   lead_x_change =block_size
                   lead_y_change = 0
                   
                elif event.key == pygame.K_UP:
                   lead_y_change = -block_size
                   lead_x_change = 0
                   
                elif event.key == pygame.K_DOWN:
                   lead_y_change =block_size
                   lead_x_change = 0
                 
       if lead_x >=display_width or lead_x<0 or lead_y>=display_hight or lead_y<0:
         gameOver = True

       lead_x += lead_x_change 
       lead_y += lead_y_change

       gameDisplay.fill(white)
       pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,block_size,block_size])

       
       snakeHead = []
       snakeHead.append(lead_x)
       snakeHead.append(lead_y)
       snakeList.append(snakeHead)
       if len(snakeList) > snakeLength:
           del snakeList[0]

       for eachSegment in snakeList[:-1]:
           if eachSegment == snakeHead:
               gameOver = True

           
       snake(block_size, snakeList)
       
       pygame.display.update()
       if lead_x == randAppleX and lead_y ==  randAppleY:
          randAppleX =round(random.randrange(0, display_width-block_size)/10.0)*10.0
          randAppleY = round(random.randrange(0, display_hight-block_size )/10.0)*10.0
          snakeLength += 1
##          point += 1
##          print(point)
##          message_to_screen("U just gain point", red)
##          pygame.display.update()
##          time.sleep(.3)
       clock.tick(FPS)
   
    pygame.quit()
    quit()

gameLoop()
