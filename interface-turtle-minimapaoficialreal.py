#desenha o minimapa utilizado na interface da câmera
import turtle
#iniciar o turtle
turtle.hideturtle()
turtle.speed(0)#modo mais rápido
turtle.tracer(0, 0)#desabilitar a animação
turtle.setup(width=1000, height=900)#mudar para tamanho ideal de janela
turtle.bgcolor("white")#background branco
#função para desenhar todas as estruturas retangulares da imagem
def desenhar_quadrado():
    turtle.color("black")#cor da linha preta
    #fazer quadrado de 400 por 90
    for _ in range(4):
        turtle.forward(400)
        turtle.right(90)
    #mesas da esquerda
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(180)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(180)
#mesas da direita
    turtle.penup()
    turtle.goto(400, -100)
    turtle.pendown()
    turtle.forward(-150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(-150)
    turtle.right(180)
    turtle.penup()
    turtle.goto(400, -250)
    turtle.pendown()
    turtle.forward(-150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(-150)
    turtle.right(180)
desenhar_quadrado()#chamando a função
#desenhar os 24 bancos circulares
def desenhar_circulo():
    turtle.penup()
    turtle.goto(375, -340)
    turtle.pendown()
    turtle.color("gray")#definir cor cinza para cada banco
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(325, -340)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(275, -340)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(275, -240)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(325, -240)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(375, -240)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(375, -190)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(325, -190)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(275, -190)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(275, -90)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(325, -90)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(375, -90)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(25, -90)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(75, -90)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(125, -90)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(125, -190)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(75, -190)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(25, -190)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(25, -240)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(75, -240)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(125, -240)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(125, -340)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(75, -340)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(25, -340)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
desenhar_circulo()#chamar função
#voltar ao inicio o turtle
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.update()#reiniciar a interface
turtle.done()
