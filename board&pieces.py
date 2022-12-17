import pygame

pygame.init()

screen=pygame.display.set_mode([800,800])
screen.fill((200,200,150))
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
def make_chessboard():
     make_collum(0,0)
     make_collum(100,1)
     make_collum(200,2)
     make_collum(300,3)
     make_collum(400,4)
     make_collum(500,5)
     make_collum(600,6)
     make_collum(700,7)
make_chessboard()
wpawn=pygame.image.load('wpawn.png').convert()
bpawn=pygame.image.load('bpawn.png').convert()
wrook=pygame.image.load('wrook.png').convert()
brook=pygame.image.load('brook.png').convert()
wqueen=pygame.image.load('wqueen.png').convert()
bqueen=pygame.image.load('bqueen.png').convert()
bbishop=pygame.image.load('bbishop.png').convert()
wbishop=pygame.image.load('wbishop.png').convert()
bknight=pygame.image.load('bknight.png').convert()
wknight=pygame.image.load('wknight.png').convert()
wking=pygame.image.load('wking.png').convert()
bking=pygame.image.load('bking.png').convert()

def put_pieces():
    px=20
    count=0
    screen.blit(wrook,(725,725))
    screen.blit(wrook,(25,725))
    screen.blit(brook,(725,25))
    screen.blit(brook,(25,25))
    screen.blit(bknight,(620,25))
    screen.blit(bknight,(125,25))
    screen.blit(wknight,(620,725))
    screen.blit(wknight,(125,725))
    screen.blit(wbishop,(220,725))
    screen.blit(wbishop,(520,725))
    screen.blit(bbishop,(220,25))
    screen.blit(bbishop,(520,25))
    screen.blit(wqueen,(420,725))
    screen.blit(bqueen,(420,25))
    screen.blit(bking,(320,25))
    screen.blit(wking,(320,725))
    while count<8:
        count+=1
        screen.blit(wpawn,(px,620))
        screen.blit(bpawn,(px,120))
        px+=100
make_chessboard()
put_pieces()
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
pygame.quit()
