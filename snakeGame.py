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



for posicao in starting_positions:
    criar_segmento(posicao) 



aim_x = PASSO #horizontal
aim_y = 0 #vertical

def ir_para_cima():
    if aim_y != -PASSO: #impede que a cobra se mova para baixo se estiver indo para cima
        global aim_x, aim_y #global avisa que essas variaveis tem que ser mudadas fora da funcao, e nao criadas cópias dentro da funcao
        aim_x = 0
        aim_y = PASSO

def ir_para_baixo():
    if aim_y != PASSO: #impede que a cobra se mova para cima se estiver indo para baixo
        global aim_x, aim_y
        aim_x = 0
        aim_y = -PASSO

def ir_para_esquerda():
    if aim_x != PASSO:
        global aim_x, aim_y
        aim_x = -PASSO
        aim_y = 0

def ir_para_direita():
    if aim_x != -PASSO:
        global aim_x, aim_y
        aim_x = PASSO
        aim_y = 0

screen.listen() #faz a tela obedecer os eventos do teclado
screen.onkey(ir_para_cima, "Up")
screen.onkey(ir_para_baixo, "Down")
screen.onkey(ir_para_esquerda, "Left")
screen.onkey(ir_para_direita, "Right")



def mover():
    novo_x = segments[0].xcor() + aim_x #segments[0] é a CABEÇA da cobra (o primeiro segmento da lista)
    #.xcor() pega a posição X atual dela na tela
    #somamos aim_x (do passo 1) pra calcular pra onde ela deve ir no eixo X
    #ex: se está em x=100 e aim_x=20, novo_x vira 120 (andou 20px pra direita)
    novo_y = segments[0].ycor() + aim_y 
    segments[0].goto(novo_x, novo_y)   #move de fato a cabeça para a nova posição calculada
    screen.update()
    screen.ontimer(mover, 100) #isso agenda: "daqui a 100 milissegundos (0.1 segundo), chame a função
mover()
screen.exitonclick() #mantém a janela aberta até você clicar nela pra fechar





