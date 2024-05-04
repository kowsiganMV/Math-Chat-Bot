def cylindervolume(h,r):
    if (h>0)and(r>0):
        return 3.14*(r**2)*h
    else:
        return("the volume does not exist")
def cylindercurvedsurfacearea(h,r):
    if (h>0)and(r>0):
        return 2*3.14*r*h
    else:
        return("the curvedsurfacearea does not exist")
def cylindertotalsurfacearea(r,h):
    if (h>0)and(r>0):
        return 2*3.14*r*(h+r)
    else:
        return("the totalsurfacearea does not exist")
#print(cylindervolume(5,6))
#print(cylindercurvedsurfacearea(5,6))
#print(cylindertotalsurfacearea(4,5))

#---------------------------------------

def conevolume(h,r):
    if (h>0)and(r>0):
        return 1/3*3.14*r**2*h
    else:
        return("the volume does not exist")
def conecurvedsurfacearea(r,l):
    if (l>0)and(r>0):
        return 3.14*r*l
    else:
        return("the curvedsurfacearea does not exist")
def conetotalsurfacearea(r,l):
    if (l>0)and(r>0):
        return 3.14*r*(l+r)
    else:
        return("the totalsurfacearea does not exist")
#print(conevolume(3,4))
#print(conecurvedsurfacearea(4,5))
#print(conetotalsurfacearea(4,5))

#---------------------------------------

def spherevolume(r):
    if (r>0):
        return 4/3*3.14*r**3
    else:
        return("the volume does not exist")
def spherecurvedsurfacearea(r):
    if (r>0):
        return 4*3.14*r**2
    else:
        return("the curvedsurfacearea does not exist")
def spheretotalsurfacearea(r):
    if (r>0):
        return 4*3.14*r**2
    else:
        return("the totalsurfacearea does not exist")
#print(spherevolume(4))
#print(spherecurvedsurfacearea(4))
#print(spheretotalsurfacearea(4))

#---------------------------------------

def hemispherevolume(r):
    if (r>0):
        return 2/3*3.14*r**3
    else:
        return("the volume does not exist")
def hemispherecurvedsurfacearea(r):
    if (r>0):
        return 2*3.14*r**2
    else:
        return("the curvedsurfacearea does not exist")
def hemispheretotalsurfacearea(r):
    if (r>0):
        return 3*3.14*r**2
    else:
        return("the totalsurfacearea does not exist")
#print(hemispherevolume(5))
#print(hemispherecurvedsurfacearea(5))
#print(hemispheretotalsurfacearea(5))

#---------------------------------------

def cubevolume(a):
    if (a>0):
        return a**3
    else:
        return("the volume does not exist")
def cubelateralsurfacearea(a):
    if (a>0):
        return 4*(a**2)
    else:
        return("the lateralsurfacearea does not exist")
def cubetotalsurfacearea(a):
    if (a>0):
        return 6*(a**2)
    else:
        return("the totalsurfacearea does not exist")
#print(cubevolume(10))
#print(cubelateralsurfacearea(10))
#print(cubetotalsurfacearea(10))

#----------------------------------------------

def cuboidvolume(l,b,h):
    if (l>0)and(b>0)and(h>0):
        return l*b*h
    else:
        return("the volume does not exist")
def cuboidlateralsurfacearea(l,b,h):
    if (l>0)and(b>0)and(h>0):
        return 2*h*(l+b)
    else:
        return("the lateralsurfacearea does not exist")
def cuboidtotalsurfacearea(l,b,h):
    if (l>0)and(b>0)and(h>0):
        return 2*(l*b+b*h+l*h)
    else:
        return("the totalsurfacearea does not exist")
#print(cuboidvolume(2,3,5))
#print(cuboidlateralsurfacearea(2,3,5))
#print(cuboidtotalsurfacearea(2,3,5))

#-----------------------------------------------

 


