#coding:utf-8

import pygame
from pygame.locals import *

# pygameの初期化
pygame.init()

# 画面を作る
screen = pygame.display.set_mode( (300, 300) )

# タイトルを設定
pygame.display.set_caption('Hello World')

# フォントを設定する
font = pygame.font.Font(None, 32)
text = font.render('Hello World!', False, (255,255,255))

while 1:
    # 画面に文字を書く
    screen.blit(text, (0,0))

    # 画面を更新して、変更を反映する
    pygame.display.flip()

    # イベントチェック
    for event in pygame.event.get():
        # 終了ボタンが押された場合
        if event.type == QUIT:
            exit()
        # ESCキーが押された場合
        if (event.type == KEYDOWN and event.key  == K_ESCAPE):
            exit()

