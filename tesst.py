 #coding:utf-8


#ステレオで音声


import pygame.time
import pygame.mixer
  
pygame.mixer.init()
  
stereoSound = pygame.mixer.Sound('cat1.wav')
 

#pygame.time.wait(1000)

stereoSound.play()
while pygame.mixer.get_busy():
	pass

