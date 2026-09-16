from turtle import Screen, Turtle
import time

screen = Screen() 
screen.setup(width=600, height=600)
screen.bgcolor("green yellow")
screen.title("Snake Game")
screen.tracer(0) #desativa a animacao da tela

PASSO = 20
LIMITE = 200



segments = [] #lista vazia para armazenar os segmentos da cobra
starting_positions = [(0, 0), (-20, 0), (-40, 0)] #posicoes em x e y para os segmentos da cobra (sao 3)

def criar_segmento(posicao):
    novo_segmento = Turtle("square") #cria um segmento da cobra
    novo_segmento.color("black") #cor do segmento
    novo_segmento.penup() #desativa o desenho do segmento
    novo_segmento.shapesize(1,1)
    novo_segmento.goto(posicao) #posiciona o segmento na posicao especificada
    segments.append(novo_segmento) #adiciona o segmento na lista de segmentos

 ################# screen.update()

for posicao in starting_positions:
    criar_segmento(posicao) 


################## screen.exitonclick()





    