'''难点:坐标点的确定
用坐标系画出来可方便确定点的位置

'''




#导入海龟画图
import turtle

#设置画笔的宽度和颜色
turtle.width(2)
turtle.color("red")

#第一个矩形
turtle.penup()
turtle.goto(100,100)
turtle.pendown()

turtle.goto(100,300)
turtle.goto(300,300)
turtle.goto(300,100)
turtle.goto(100,100)

#第二个矩形
turtle.penup()
turtle.goto(100,-100)
turtle.pendown()

turtle.goto(100,-300)
turtle.goto(300,-300)
turtle.goto(300,-100)
turtle.goto(100,-100)


#第三个矩形
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()

turtle.goto(-100,-300)
turtle.goto(-300,-300)
turtle.goto(-300,-100)
turtle.goto(-100,-100)

#第四个矩形
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()

turtle.goto(-100,300)
turtle.goto(-300,300)
turtle.goto(-300,100)
turtle.goto(-100,100)



