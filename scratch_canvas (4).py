import turtle,random

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
color = ['red', 'pink', 'orange', 'cyan', 'blue', 'black']

def draw_lines(a, b):
    for value in a:
        turtle.forward(value)
        turtle.pencolor(random.choice(b))
        (turtle.stamp())
        turtle.backward(value)
        turtle.right(30)
        a.append(value + 20)
        a.remove(value)
       
draw_lines(l,color)