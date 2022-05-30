import turtle as t

# define a velocidade da turtle
t.speed(2)

#linha radical
for i in range(6):
   t.forward(92)
   t.backward(92)
   t.right(60)

# comprimento da linha espiral
side = 50

# Cor da teia de aranha
t.fillcolor("Red")

#construindo web
t.begin_fill()

for i in range(15):
   t.penup()
   t.goto(0, 0)
   t.pendown()
   t.setheading(0)
   t.forward(side)
   t.right(120)
   
   # Inner for loop de alcance 6
   for j in range (6):
      t.forward(side-2)#para cada lado da iteração diminui em 2
      
      t.right(60)
   side = side - 10 #O lado diminui em 10
   
#Cor de preenchimento é concluída
t.end_fill()