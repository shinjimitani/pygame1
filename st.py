 #coding:utf-8


#ステレオで音声


import pygame.time
import pygame.mixer
  
pygame.mixer.init()
  
#monoSound = pygame.mixer.Sound('cat1.wav')
stereoSound = pygame.mixer.Sound('cat1.wav')
 
#monoSound.play()


#while pygame.mixer.get_busy():
#	pass
 
pygame.time.wait(1000)

stereoSound.play()
while pygame.mixer.get_busy():
	pass

