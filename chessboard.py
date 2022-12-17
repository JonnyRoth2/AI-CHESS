import pygame

pygame.init()

screen=pygame.display.set_mode([800,800])

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
    screen.fill((255,255,255))
    def make_collum(x:int,collum_num:int):
        count=0
        recty=0
        while count<8:
            count+=1
            recty+=100
            if collum_num%2==0:
                pygame.draw.rect(screen,(0,0,0),(x,0,100,100))
                if count%2==0:
                    pygame.draw.rect(screen,(0,0,0),(x,recty,100,100))
            else:
                if count%2==1:
                    pygame.draw.rect(screen,(0,0,0),(x,recty,100,100))
    make_collum(0,0)
    make_collum(100,1)
    make_collum(200,2)
    make_collum(300,3)
    make_collum(400,4)
    make_collum(500,5)
    make_collum(600,6)
    make_collum(700,7)
    pygame.display.flip()
pygame.quit()
