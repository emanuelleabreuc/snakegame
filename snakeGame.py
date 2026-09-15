from turtle import Screen, Turtle

screen = Screen() 
screen.setup(width=600, height=600)
screen.bgcolor("green yellow")
screen.title("Snake Game")
screen.tracer(0)

screen.exitonclick() 

segments = [] #lista vazia para armazenar os segmentos da cobra
starting_positions = [(0, 0), (-20, 0), (-40, 0)] #posicoes em x e y para os segmentos da cobra (sao 3)
for posicao in starting_positions:
    novo_segmento = Turtle("square") 
    novo_segmento.color("black")
    novo_segmento.penup() #perguntar pra raissa
    novo_segmento.shapesize(1,1)
    novo_segmento.goto(posicao) #coloca a cobra na posicao inicial
    segments.append(novo_segmento)

screen.update()



    