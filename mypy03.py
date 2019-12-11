#绘制奥运五环

import turtle as t

t.width(10)


#第一个环
t.color("blue")
t.circle(50)
#第二个环
t.color("black")
t.penup()
t.goto(120,0)
t.pendown()
t.circle(50)
#第三个环
t.color("red")
t.penup()
t.goto(240,0)
t.pendown()
t.circle(50)
#第四个环
t.color("yellow")
t.penup()
t.goto(60,-50)
t.pendown()
t.circle(50)
#第五个环
t.color("green")
t.penup()
t.goto(180,-50)
t.pendown()
t.circle(50)
