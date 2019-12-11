import turtle,math

#定义多个点
x1,y1 = 10,170
x2,y2 = 100,-150
x3,y3 = -400,-100
x4,y4 = -4,55

#绘制折线
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

#计算起始点到终点的距离
dis = math.sqrt((x1-x4)**2+(y1-y4)**2)

turtle.write(dis)
