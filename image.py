import turtle 

from turtle import *
color('red', 'yellow')
# Turtle will draw two lines and then continue following the path until a shape is formed
begin_fill()
while True:
    forward(50)
    left(50)
    # right(20)
    if abs(pos()) < 1:
        break
end_fill()
done()