import pygame, sys
from pygame.locals import *


class Termometro():
    
    termometro= None
    entrada= None
    selector= None
    

    def __init__(self, x=0, y=0):
        self.__screen= pygame.display.set_mode((290, 415))  #creacion de la pantalla  
        pygame.display.set_caption("Conversor de temperatura")     # titulo de la pantalla
        self.__screen.fill((200,250,0))  #imagen de fondo
        self.custom= pygame.image.load("Images/{}.png".format('termo1'))
        

    def __onClose(self):
        pygame.quit()
        sys.exit()
  
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__onClose()
                    
            self.__screen.blit(self.custom, (50,34))
            pygame.display.flip()



if __name__=="__main__":
    pygame.init()
    t= Termometro()
    t.start()