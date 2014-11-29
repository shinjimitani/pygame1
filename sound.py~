#coding:utf-8

import pygame
from pygame.locals import *
import sys


#イベントハンドラー
#for event in pygame.event.get():
#        if event.type == QUIT:
#            sys.exit()
        # マウスクリックで蛇をコピー
#        if event.type == MOUSEBUTTONDOWN and event.button == 1:
#            x, y = event.pos
#            x -= pythonImg.get_width() / 2
#            y -= pythonImg.get_height() / 2
#            pythons_pos.append((x,y))  # 蛇の位置を追加
        # マウス移動で蛇を移動
#        if event.type == MOUSEMOTION:
#            x, y = event.pos
#            x -= pythonImg.get_width() / 2
#            y -= pythonImg.get_height() / 2
#            cur_pos = (x,y)




SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Hello, world!")

# フォントの作成
sysfont = pygame.font.SysFont(None, 80)
# テキストを描画したSurfaceを作成
hello1 = sysfont.render("Hello, world!", False, (0,0,0))
hello2 = sysfont.render("Hello, world!", True, (0,0,0))
hello3 = sysfont.render("Hello, world!", True, (255,0,0), (255,255,0))

while True:
    screen.fill((0,0,255))
    
    # テキストを描画する
    screen.blit(hello1, (20,50))
    screen.blit(hello2, (20,150))
    screen.blit(hello3, (20,250))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        # マウスクリックで蛇をコピー
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			print 'aaaaaaaaaa'

		if event.type == KEYDOWN:#
			if event.key == K_ESCAPE:
				sys.exit()


#if event.type == QUIT:
#            sys.exit()
