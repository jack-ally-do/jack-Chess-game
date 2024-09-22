import pygame

pygame.init()
screen=pygame.display.set_mode((750,750))
pygame.display.set_caption('gobang')
player=1
list_1=[0]*15
for i in range(15):
    list_1[i]=[0]*15
winter=0
running=True
def five(row,col):
    sore=1
    for i in range(4):
        if list_1[row][col+i]==list_1[row][col+i+1]:
            sore=sore+1
        else:
            break
    for i in range(4):
        if list_1[row][col-i]==list_1[row][col-i-1]:
            sore=sore+1
        else:
            break
    for i in range(4):
        if list_1[row+i][col]==list_1[row+i+1][col]:
            sore=sore+1
        else:
            break
    for i in range(4):
        if list_1[row-i][col]==list_1[row-i-1][col]:
            sore=sore+1
        else:
            break
    for i in range(4):
        if list_1[row+i][col+i]==list_1[row+i+1][col+i+1]:
            sore=sore+1
        else:
            break
    for i in range(4):
        if list_1[row-i][col-i]==list_1[row-i-1][col-i-1]:
            sore=sore+1
        else:
            break
    for i in range(4):
        if list_1[row+i][col-i]==list_1[row+i+1][col-i-1]:
            sore=sore+1
        else:
            break
    for i in range(4):
        if list_1[row-i][col+i]==list_1[row-i-1][col+i+1]:
            sore=sore+1
        else:
            break
    if sore==5:
        return True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            col=round((x-25)/50)
            row=round((y-25)/50)
            
            if list_1[row][col]==0:
                print(row,col)
                list_1[row][col]=player
                if(five(row,col)):
                    if player==1:
                        winter=1
                        player=2
                    elif player==2:
                        winter=2
                        player=1
                else:
                    if player==1:
                        player=2
                    else:
                        player=1
            else:
                print('已经有有棋子')



    screen.fill('#EE9A49')
    for x in range(15):
        pygame.draw.line(screen,'#000000',[25+50*x,25],[25+50*x,725],1)
    for y in range(15):
        pygame.draw.line(screen,'#000000',[25,25+50*y],[725,25+50*y],1)
    pygame.draw.circle(screen,'#000000',[25+50*7,25+50*7],8)
    x,y=pygame.mouse.get_pos()
    x=round((x-25)/50)*50+25
    y=round((y-25)/50)*50+25
    for row in range(15):
        for col in range(15):
            if list_1[row][col]==1:
                pygame.draw.circle(screen,'#000000',[col*50+25,row*50+25],25)
            if list_1[row][col]==2:
                pygame.draw.circle(screen,'#FFFFFF',[col*50+25,row*50+25],25)
    pygame.draw.rect(screen,'#FFFFFF',[x-25,y-25,50,50],2)
    if(winter!=0):
        if winter==1: 
            text=' white is win '
            color=(255,255,255)
        else:
            text=' black is win '
            color=(0,0,0)
        font=pygame.font.Font('font.ttf',70)
        text_surf=font.render(text,True,color)
        position_surf=(100,150)
        screen.blit(text_surf,position_surf)
        
        
    pygame.display.update()
    
pygame.quit()