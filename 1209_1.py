#coding:utf-8

#初版2014/12/09
#
#
#
#





import pygame
from pygame.locals import *
import sys

import pygame.time
import pygame.mixer
  
pygame.mixer.init()
  

def sound():#sound
	stereoSound = pygame.mixer.Sound('cat1.wav') 
#pygame.time.wait(1000)

	stereoSound.play()
	while pygame.mixer.get_busy():
		pass


SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Sound")

# フォントの作成
sysfont = pygame.font.SysFont(None, 80)
# テキストを描画したSurfaceを作成

hello1 = sysfont.render(u"esc ", False, (0,0,0))
clock=pygame.time.Clock()
i=20
while True:
	clock.tick(60)
 
	screen.fill((0,0,255))#blue
    
    # テキストを描画する
	screen.blit(hello1, (i,50))
    
	pygame.display.update()
    	i +=1
	for event in pygame.event.get():
        # マウスクリック
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			print 'aaaaaaaaaa'
			sound()

		if event.type == KEYDOWN:#
			if event.key == K_ESCAPE:
				sys.exit()


		if event.type == QUIT:
	            sys.exit()
