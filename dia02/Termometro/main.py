import pygame, sys
from pygame.locals import *



class NumberInput():
    __value=0
    __position=(0,0)
    __size=(0,0)
    __strValue='0'
    
    def __init__(self, value=0):
        self.__font= pygame.font.SysFont('Arial', 24)
        self.value(value)
        
    def onEvent(self, event):
        if event.type== KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue)< 10:
                self.__strValue += event.unicode
            elif event.key== K_BACKSPACE:
                self.__strValue= self.__strValue[0:-1]
    
    def render(self):
        textBlock= self.__font.render(self.__strValue, True, (74,74,74))   #esto pinta el cuadro con  la temperatura que ponemos. Tiene que ser una cadena pq render solo pinta cadenas
        
        rect= textBlock.get_rect()
        rect.left=self.__position[0]
        rect.top=self.__position[1]
        rect.size= self.__size
        
        return (rect, textBlock)
        
        
        
# métodos getter y setter para validar que la entrada de datos, tanto de
# valor de temperatura como de tamaño y posicion de pantala, son correctos.
    def value(self, val= None):
        if val== None:
            return self.__value
        else:
            val= str(val)
            try:
                self.__value= int(val)
                self.__strValue= val
            except:
                pass
            
    def width(self, val= None):
        if vale==None:
            return self.__size[0]
        else:
            try:
                self.__size[0]= int(val)
            except:
                pass
            
    def height(self, val= None):
        if vale==None:
            return self.__size[1]
        else:
            try:
                self.__size[1]= int(val)
            except:
                pass
        
    def size(self, val= None):
        if val== None:
            return self.__size
        else:
            try:
                w= int(val[0])
                h= int(val[1])
                self.__size= [w,h]
            except:
                pass


    def posX(self, val= None):
        if vale==None:
            return self.__position[0]
        else:
            try:
                self.__position[0]= int(val)
            except:
                pass
            
    def posY(self, val= None):
        if vale==None:
            return self.__position[1]
        else:
            try:
                self.__position[1]= int(val)
            except:
                pass
        
    def pos(self, val= None):
        if val== None:
            return self.__position
        else:
            try:
                x= int(val[0])
                y= int(val[1])
                self.__position= [x,y]
            except:
                pass


class Termometro():
    
    termometro= None
    entrada= None
    selector= None
    

    def __init__(self):
        self.__screen= pygame.display.set_mode((290, 415))  #creacion de la pantalla  
        pygame.display.set_caption("Conversor de temperatura")     # titulo de la pantalla
        self.__screen.fill((200,250,0))  #imagen de fondo
        self.custom= pygame.image.load("Images/{}.png".format('termo1'))
        
        self.entrada= NumberInput(0)
        self.entrada.pos((106,58))
        self.entrada.size((133,28))

    def __onClose(self):
        pygame.quit()
        sys.exit()
  
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__onClose()
                    
                self.entrada.onEvent(event)
            
                    
                    
            #ponemos el termometro en su posicion
            self.__screen.blit(self.custom, (50,34))
            #pintamos el cuadro de texto
            text=self.entrada.render()
            pygame.draw.rect(self.__screen,(255,255,255), text[0]) #rectangulo blanco con su posicion y tamañap
            self.__screen.blit(text[1], self.entrada.pos())       #este es el texto, el  numero de la temperatura
            
            
                
            pygame.display.flip()



if __name__=="__main__":
    pygame.init()
    t= Termometro()
    t.start()