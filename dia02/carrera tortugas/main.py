import turtle
import random


class Circuito():
    corredores= []
    __posStartY=(-60, -20, 20, 60)
    __colorTurtle=('red', 'green', 'yellow', 'blue')
    
    
    def __init__(self, width, height):
        self.__screen= turtle.Screen()      #modulo de Turtle q diseña la pantalla
        self.__screen.setup(width, height)  #tamaño de la pantalla.
        self.__screen.bgcolor('lightgray')   #color de fondo de la pantalla
        self.__startLine= -width/2 + 20     # coordenadas de posicion salida
        self.__finishLine= width/2 -20     #posicion llegada
        
        self.__runners()
        
        
    def __runners(self):
        for i in range (4):
            new_turtle= turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.penup()   #para que no punten rayas las tortugas cuando se mueven
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
        #con el for, creamos los 4 corredores (new_turtle) y se añaden a la lista corredores.
        
        
    def competir (self):
        ganador= False
        
        while not ganador:
            for tortuga in self.corredores:
                avance= random.randint(1,6)
                tortuga.forward(avance)   #instruccion del modulo Turtle para que la tortuga avance el nº que ha salido de random
                
                if tortuga.position()[0] >= self.__finishLine:
                    ganador= True
                    print("Ha ganado la tortuga {}".format (tortuga.color()[0]))
                    break
    
    
    
    
if __name__== '__main__':       #si se ejecuta desde main, la pantalla
    circuito= Circuito (640, 480)  # tiene estas dimensiones. Y si importamos este modulo a otro, esta parte no se ejecutaria.
    
    circuito.competir()