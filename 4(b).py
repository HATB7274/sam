def calc(x1,y1,x2,y2):
    d=0
    d=((((x2-x1)**2)+((y2-y1)*2)))**0.5
    print("The distance between",(x1,x2),"and",(y1,y2),"is:",d)
x1=eval(input("Enter the value of point1(x1,y1)"))
y1=eval(input())
x2=eval(input("Enter the value of point2(x2,y2)"))
y2=eval(input())
calc(x1,y1,x2,y2)
