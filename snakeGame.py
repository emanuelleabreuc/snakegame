from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green yellow")
screen.title("Snake Game")
screen.tracer(0)  # desativa a animacao da tela

PASSO = 20
LIMITE = 280

segments = []  # lista vazia para armazenar os segmentos da cobra
starting_positions = [(0, 0), (-20, 0), (-40, 0)]  # posicoes em x e y para os segmentos da cobra (sao 3)


def criar_segmento(posicao):
    novo_segmento = Turtle("square")  # cria um segmento da cobra
    novo_segmento.color("black")  # cor do segmento
    novo_segmento.penup()  # desativa o desenho do segmento
    novo_segmento.shapesize(1, 1)
    novo_segmento.goto(posicao)  # posiciona o segmento na posicao especificada
    segments.append(novo_segmento)  # adiciona o segmento na lista de segmentos


for posicao in starting_positions:
    criar_segmento(posicao)


aim_x = PASSO  # horizontal
aim_y = 0  # vertical


def ir_para_cima():
    global aim_x, aim_y
    if aim_y != -PASSO:  # impede que a cobra se mova para baixo se estiver indo para cima
        aim_x = 0
        aim_y = PASSO


def ir_para_baixo():
    global aim_x, aim_y
    if aim_y != PASSO:  # impede que a cobra se mova para cima se estiver indo para baixo
        aim_x = 0
        aim_y = -PASSO


def ir_para_esquerda():
    global aim_x, aim_y
    if aim_x != PASSO:
        aim_x = -PASSO
        aim_y = 0


def ir_para_direita():
    global aim_x, aim_y
    if aim_x != -PASSO:
        aim_x = PASSO
        aim_y = 0


screen.listen()  # faz a tela obedecer os eventos do teclado
screen.onkey(ir_para_cima, "Up")
screen.onkey(ir_para_baixo, "Down")
screen.onkey(ir_para_esquerda, "Left")
screen.onkey(ir_para_direita, "Right")


def mover():
    posicoes = [segmento.pos() for segmento in segments]  # pra cada segmento da cobra, pega a posicao atual e armazena na lista posicoes

    for i in range(len(segments) - 1, 0, -1):  # percorre a lista de segmentos da cobra de tras pra frente, comecando do ultimo segmento ate o primeiro
        segments[i].goto(posicoes[i - 1])  # faz o segmento atual ir para a posicao do segmento anterior, fazendo com que a cobra se mova

    novo_x = segments[0].xcor() + aim_x  # calcula a nova posicao do primeiro segmento da cobra, somando a posicao atual com o valor de aim_x e aim_y
    novo_y = segments[0].ycor() + aim_y
    segments[0].goto(novo_x, novo_y)  # faz o primeiro segmento da cobra ir para a nova posicao calculada

    if abs(segments[0].xcor()) > LIMITE or abs(segments[0].ycor()) > LIMITE:  # verifica se o segmento x e y da cobra ultrapassou os limites da tela, se sim, imprime "Game Over" e encerra o jogo
        print("Game Over")
        screen.update()
        return

    for segmento in segments[1:]:  # verifica se a cobra colidiu com ela mesma
        if segments[0].distance(segmento) < 10:
            print("Game Over")
            screen.update()
            return

    screen.update()  # atualiza a tela
    screen.ontimer(mover, 100)  # chama a funcao mover a cada 100 milissegundos


comida = Turtle("circle")  # cria a comida da cobra
comida.color("red")
comida.penup()  # n deixa rastro
comida.shapesize(0.5, 0.5)


def reposicionar_comida():
    random_x = random.randint(-LIMITE + 20, LIMITE - 20)
    random_y = random.randint(-LIMITE + 20, LIMITE - 20)
    comida.goto(random_x, random_y)

reposicionar_comida()

score = 0  # inicializa a pontuacao do jogador

<<<<<<< HEAD
def colisao(): 
=======
def colisao() 
>>>>>>> 59f09e54cf25262a46a9613ce72f5c5348bdc47d
    if segments[0].distance(comida) < 15:  # verifica se a cobra colidiu com a comida
        reposicionar_comida()  # reposiciona a comida em uma nova posicao aleatoria
        criar_segmento(segments[-1].pos())  # cria um novo segmento da cobra na posicao do ultimo segmento
        global score
        score += 1  # incrementa a pontuacao do jogador
        print(f"Score: {score}")

screen.update()
screen.ontimer(mover, 100)
mover()  # inicia o movimento da cobra
<<<<<<< HEAD

screen.onkey(ir_para_cima, "w")
screen.onkey(ir_para_baixo, "s")
screen.onkey(ir_para_esquerda, "a")
screen.onkey(ir_para_direita, "d")



screen.exitonclick()
=======
screen.exitonclick()
>>>>>>> 59f09e54cf25262a46a9613ce72f5c5348bdc47d
