import math



def rectanglearea(a,b):
    if a>0 and b>0:
        return(a*b)
    else:
        return("The area does not exist")
def rectangleperimeter(a,b):
    if a>0 and b>0:
        return(2*(a+b))
    else:
        return("The perimeter does not exist")
#print(rectanglearea(2,4))
#print(rectangleperimeter(-2,4))
#-----------------------------------------------------
def squarearea(a):
    if a>0:
         return(a**2)
    else:
        return("The area does not exist")
def squareperimeter(a):
    if a>0:
        return(4*a)
    else:
        return("The perimeter does not exist")
#print(squarearea(2))
#print(squareperimeter(-2))
#--------------------------------------------------
def trianglearea(b,h):
    if b>0 and h>0:
         return((1/2)*b*h)
    else:
        return("The area does not exist")
def triangleperimeter(a,b,c):
    if a>0 and b>0 and c>0:
        return(a+b+c)
    else:
        return("The perimeter does not exist")
#print(trianglearea(2,4))
#print(triangleperimeter(2,4,2))
#---------------------------------------------------
def righttrianglearea(b,h):
    if h>0 and b>0:
         return((1/2)*b*h)
    else:
        return("The area does not exist")
def righttriangleperimeter(b,h):
    if b>0 and h>0 :
        return(b+h+math.sqrt((b**2)+(h**2)))
    else:
        return("The perimeter does not exist")
#print(trianglearea(2,4))
#print(triangleperimeter(2,4,2))        
#-----------------------------------------------------------------
def equilateraltrianglearea(a):
    if a>0:
         return((0.433)*(a**2))
    else:
        return("The area does not exist")
def equilateraltriangleperimeter(a):
    if a>0:
        return(3*a)
    else:
        return("The perimeter does not exist")
#print(equilateraltrianglearea(2,4))
#print(equilateraltriangleperimeter(2))
#----------------------------------------------------------------
def isoscelesrighttrianglearea(a):
    if a>0:
         return((1/2)*(a**2))
    else:
        return("The area does not exist")
def isoscelesrighttriangleperimeter(a,d):
    if a>0 and d>0:
        return((2*a)+d)
    else:
        return("The perimeter does not exist")
#print(isoscelesrighttrianglearea(2,4))
#print(isoscelesrighttriangleperimeter(2,4))           
#------------------------------------------------------
def parallelogramarea(a,h):
    if a>0 and h>0:
         return(a*h)
    else:
        return("The area does not exist")
def parallelogramperimeter(a,b):
    if a>0 and b>0:
        return(2*(a+b))
    else:
        return("The perimeter does not exist")
#print(parallelogramarea(2,4))
#print(parallelogramperimeter(2,4)) 
#----------------------------------------------
def rhombusarea(d1,d2):
    if d1>0 and d2>0:
         return((1/2)*d1*d2)
    else:
        return("The area does not exist")
def rhombusperimeter(a):
    if a>0:
        return(4*a)
    else:
        return("The perimeter does not exist")
#print(rhombusarea(2,4))
#print(rhombusperimeter(4))     
#-------------------------------------------
def trapeziumarea(a,b,h):
    if a>0 and b>0 and h>0:
         return((1/2)*h*(a+b))
    else:
        return("The area does not exist")
def trapeziumperimeter(a,b,c,d):
    if a>0 and b>0 and c>0 and d>0:
        return(a+b+c+d)
    else:
        return("The perimeter does not exist")
#print(trapeziumarea(2,4,2))
#print(trapeziumperimeter(2,4,2,4))     
#---------------------------------------------
def circlearea(r):
    if r>0:
         return(3.14*(r**2))
    else:
        return("The area does not exist")
def circleperimeter(r):
    if r>0:
        return(2*3.14*r)
    else:
        return("The perimeter does not exist")
#print(circlearea(2))
#print(circleperimeter(2))         
