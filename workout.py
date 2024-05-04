from algebra import *
from twoDshapes import *
import json
from threeDshapes import *
import math
import random


def finalans(Bot,tempans,name):
  botmsg=Bot
  temp=["","","","",""]
  ans="The answer  {}  ".format(name)+str(tempans)
  temp[0]=ans
  botmsg.append(temp)
  return botmsg


def Bot(user,Bot):
  f=open('data1.json',encoding="utf8")
  datas=json.load(f)
  a=user[-1].split(" ")
  try:
    for i in range(1,79):
        if "hi" in user[-1].lower()  or "hello" in user[-1].lower() or "hey" in user[-1].lower():
          botmsg=Bot
          temp=datas["1"][3]
          botmsg.append([random.choice(temp),"","",""])
          return botmsg
        if user[-1].lower() in datas[str(i)][1]:
          botmsg=Bot
          botmsg.append(datas[str(i)][2])
          return botmsg
    else:
      if user[-2].lower() in datas["14"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=aplusbholesquare(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,"a and b in (a+b)² is ")
        

    #-----------------------------   For process 2 (a-b)²   ------------------------------

      elif user[-2].lower() in datas["15"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=aminusbholesquare(int(a[0]),int(a[1])) 
          return finalans(Bot,tempans,"a and b in (a-b)² is ")

    #-----------------------------   For process 2 a²-b²   ------------------------------

      elif user[-2].lower() in  datas["16"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=asquareminusbsquare(int(a[0]),int(a[1]))
          return finalans(Bot,tempans," a and b in a²-b² is ")

  #-----------------------------   For process 2 a²+b²   ------------------------------

      elif user[-2].lower() in  datas["17"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=asquareplusbsquare(int(a[0]),int(a[1]))
          return finalans(Bot,tempans," a and b in a²+b² is ")

    #-----------------------------   For process 2 (a+b)³ or  a³+b³   ------------------------------

      elif user[-2].lower() in  datas["18"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=acubeplusbcube(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,"a and b in (a+b)³ is")

    #-----------------------------   For process 2 a³-b³  ------------------------------

      elif user[-2].lower() in  datas["19"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=acubeminusbcube(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,"a and b in (a-b)³ is")

    #-----------------------------   For process 2 a⁴+b⁴  ------------------------------
      elif user[-2].lower() in  datas["20"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=apowerfourplusbpowerfour(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,"a and b in a⁴+b⁴ is")
    #-----------------------------   For process 2 a⁸-b⁸ ------------------------------
      elif user[-2].lower() in  datas["21"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=apowereightminusbpowereight(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,"a and b in a⁸-b⁸ is")
          
  #-----------------------------   For process 2 (a+b+c)²------------------------------
      elif user[-2].lower() in  datas["22"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=aplusbpluscholesquare(int(a[0]),int(a[1]),int(a[2]))
          return finalans(Bot,tempans,"a and b and c in (a+b+c)² is")
  #-----------------------------   For process 2 (a+b-c)²------------------------------
      elif user[-2].lower() in  datas["23"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=aplusbminuscholesquare(int(a[0]),int(a[1]),int(a[2]))
          return finalans(Bot,tempans,"a and b and c in (a+b-c)² is")
  #-----------------------------   For process 2 (a-b-c)²------------------------------
      elif user[-2].lower() in  datas["24"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=aminusbminuscholesquare(int(a[0]),int(a[1]),int(a[2]))
          return finalans(Bot,tempans,"a and b and c in (a-b-c)² is")
  #-----------------------------   For process 2 (a³+b³+c³-3abc)------------------------------
      elif user[-2].lower() in  datas["25"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=acubeplusbcubeplusccubeminusthreeabc(int(a[0]),int(a[1]),int(a[2]))
          return finalans(Bot,tempans,"a and b and c in (a³+b³+c³-3abc) is")
  #-----------------------------   For process 2 (a⁴+a²b²+b⁴)------------------------------
      elif user[-2].lower() in  datas["26"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=apowerfourplusasquarebsquareplusbpowerfour(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,"a and b and c in (a⁴+a²b²+b⁴) is")


  #-----------------------------   For process 2 Area of square------------------------------
      elif user[-2].lower() in  datas["27"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=squarearea(int(a[0]))
          return finalans(Bot,tempans,f"for Area of the square with side : {a[0]} is   ")
  #-----------------------------   For process 2 Area of the rectangle ------------------------------
      elif user[-2].lower() in  datas["28"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=rectanglearea(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for Area of the rectangle with l :{a[0]} b :{a[1]} is   ")
  #-----------------------------   For process 2 Area of the triangle------------------------------
      elif user[-2].lower() in  datas["29"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=trianglearea(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for Area of the triangle with b :{a[0]} h :{a[1]} is   ")
  #-----------------------------   For process 2 Area of the right triangle------------------------------
      elif user[-2].lower() in  datas["30"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=righttrianglearea(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for Area of the right triangle with b :{a[0]} h :{a[1]} is   ")
  #-----------------------------   For process 2 Area of the equilateral triangle------------------------------
      elif user[-2].lower() in  datas["31"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=equilateraltrianglearea(int(a[0]))
          return finalans(Bot,tempans,f"for Area of the equilateral triangle with a :{a[0]} is    ")
  #-----------------------------   For process 2 Area of the isosceles right triangle------------------------------
      elif user[-2].lower() in  datas["32"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=isoscelesrighttrianglearea(int(a[0]))
          return finalans(Bot,tempans,f"for Area of the isosceles right triangle with a :{a[0]} is    ")
  #-----------------------------   For process 2 Area of the parallelogram------------------------------
      elif user[-2].lower() in  datas["33"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=parallelogramarea(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for Area of the parallelogram with a :{a[0]}  b : {a[1]} is   ")
  #-----------------------------   For process 2 Area of the rhombus------------------------------
      elif user[-2].lower() in  datas["34"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=rhombusarea(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for Area of the rhombus with D1 :{a[0]}  d2 : {a[1]} is   ")
  #-----------------------------   For process 2 Area of the trapezium------------------------------
      elif user[-2].lower() in  datas["35"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=trapeziumarea(int(a[0]),int(a[1]),int(a[2]))
          return finalans(Bot,tempans,f"for Area of the trapezium with a :{a[0]}  b : {a[1]}  h : {a[2]} is   ")
  #-----------------------------   For process 2 Area of the circle------------------------------
      elif user[-2].lower() in  datas["36"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=circlearea(int(a[0]))
          return finalans(Bot,tempans,f"for Area of the circle with r :{a[0]} is   ")


  #-----------------------------   For process 2 Perimiter of square------------------------------
      elif user[-2].lower() in  datas["37"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=squareperimeter(int(a[0]))
          return finalans(Bot,tempans,f"for Perimeter of the square with side : {a[0]} is   ")
  #-----------------------------   For process 2 Perimiter of the rectangle ------------------------------
      elif user[-2].lower() in  datas["38"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=rectangleperimeter(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for Perimiter of the rectangle with l :{a[0]} b :{a[1]} is   ")
  #-----------------------------   For process 2 Perimiter of the triangle------------------------------
      elif user[-2].lower() in  datas["39"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=triangleperimeter(int(a[0]),int(a[1]),int(a[2]))
          return finalans(Bot,tempans,f"for Perimiter of the triangle with a :{a[0]} b :{a[1]} c : {a[2]}  is   ")
  #-----------------------------   For process 2 Perimiter of the right triangle------------------------------
      elif user[-2].lower() in  datas["40"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=righttriangleperimeter(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for Perimiter of the right triangle with b :{a[0]} h :{a[1]} is   ")
  #-----------------------------   For process 2 Perimiter of the equilateral triangle------------------------------
      elif user[-2].lower() in  datas["41"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=equilateraltriangleperimeter(int(a[0]))
          return finalans(Bot,tempans,f"for Perimiter of the equilateral triangle with a :{a[0]} is    ")
  #-----------------------------   For process 2 Perimiter of the isosceles right triangle------------------------------
      elif user[-2].lower() in  datas["42"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=isoscelesrighttriangleperimeter(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for Perimiter of the isosceles right triangle with a :{a[0]} d : {a[1]} is    ")
  #-----------------------------   For process 2 Perimiter of the parallelogram------------------------------
      elif user[-2].lower() in  datas["43"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=parallelogramperimeter(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for Perimiter of the parallelogram with a :{a[0]}  b : {a[1]} is   ")
  #-----------------------------   For process 2 Perimiter of the rhombus------------------------------
      elif user[-2].lower() in  datas["44"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=rhombusperimeter(int(a[0]))
          return finalans(Bot,tempans,f"for Perimiter of the rhombus with a :{a[0]} is   ")
  #-----------------------------   For process 2 Perimiter of the trapezium------------------------------
      elif user[-2].lower() in  datas["45"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=trapeziumperimeter(int(a[0]),int(a[1]),int(a[2]),int(a[3]))
          return finalans(Bot,tempans,f"for Perimiter of the trapezium with a :{a[0]}  b : {a[1]}  c : {a[2]} d : {a[3]} is   ")
  #-----------------------------   For process 2 Perimiter of the circle------------------------------
      elif user[-2].lower() in  datas["46"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=circleperimeter(int(a[0]))
          return finalans(Bot,tempans,f"for Perimiter of the circle with r :{a[0]} is   ")
      
  #-----------------------------   For process 2 volume of cube------------------------------

      elif user[-2].lower() in  datas["47"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=cubevolume(int(a[0]))
          return finalans(Bot,tempans,f"for volume of cube with a :{a[0]} is   ")
  #-----------------------------   For process 2 volume of cuboid------------------------------

      elif user[-2].lower() in  datas["48"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=cuboidvolume(int(a[0]),int(a[1]),int(a[2]))
          return finalans(Bot,tempans,f"for volume of cuboid with r :{a[0]} and b : {a[1]} and c : {a[2]} is   ")
  #-----------------------------   For process 2 volume of cylinder------------------------------

      elif user[-2].lower() in  datas["49"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=cylindervolume(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for volume of cylinder with h :{a[0]} and r : {a[1]} is   ")
  #-----------------------------   For process 2 volume of cone------------------------------

      elif user[-2].lower() in  datas["50"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=conevolume(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for volume of cone with h :{a[0]} and r : {a[1]} is   ")
  #-----------------------------   For process 2 volume of sphere------------------------------

      elif user[-2].lower() in  datas["51"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=spherevolume(int(a[0]))
          return finalans(Bot,tempans,f"for volume of sphere with r : {a[0]} is   ")
  #-----------------------------   For process 2 volume of hemisphere------------------------------

      elif user[-2].lower() in  datas["52"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=hemispherevolume(int(a[0]))
          return finalans(Bot,tempans,f"for volume of hemisphere with r : {a[0]} is   ")
  #-----------------------------   For process 2 lateral surface area of cube------------------------------

      elif user[-2].lower() in  datas["53"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=cubelateralsurfacearea(int(a[0]))
          return finalans(Bot,tempans,f"for lateral surface area of cube with a : {a[0]} is   ")
  #-----------------------------   For process 2 lateral surface area of cuboid------------------------------

      elif user[-2].lower() in  datas["54"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=cuboidlateralsurfacearea(int(a[0]),int(a[1]),int(a[2]))
          return finalans(Bot,tempans,f"for lateral surface area of cuboid with l : {a[0]} b : {a[1]} h : {a[2]} is   ")
  #-----------------------------   For process 2 curved surface area of cylinder------------------------------

      elif user[-2].lower() in  datas["55"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=cylindercurvedsurfacearea(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for curved surface area of cylinder with h : {a[0]} r : {a[1]}  is   ")
  #-----------------------------   For process 2 curved surface area of cone------------------------------

      elif user[-2].lower() in  datas["56"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=conecurvedsurfacearea(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for curved surface area of cone with r : {a[0]} l : {a[1]}  is   ")
  #-----------------------------   For process 2 curved surface area of sphere------------------------------

      elif user[-2].lower() in  datas["57"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=spherecurvedsurfacearea(int(a[0]))
          return finalans(Bot,tempans,f"for curved surface area of cube with r : {a[0]}  is   ")
  #-----------------------------   For process 2 curved surface area of hemisphere------------------------------

      elif user[-2].lower() in  datas["58"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=hemispherecurvedsurfacearea(int(a[0]))
          return finalans(Bot,tempans,f"for curved surface area of hemisphere with r : {a[0]}  is   ")


  #-----------------------------   For process 2 total surface area of cube------------------------------

      elif user[-2].lower() in  datas["59"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=cubetotalsurfacearea(int(a[0]))
          return finalans(Bot,tempans,f"for total surface area of cube with a : {a[0]}  is   ")
  #-----------------------------   For process 2 total surface area of cuboid------------------------------

      elif user[-2].lower() in  datas["60"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=cuboidtotalsurfacearea(int(a[0]),int(a[1]),int(a[2]))
          return finalans(Bot,tempans,f"for total surface area of cuboid with l : {a[0]} b : {a[1]} h : {a[2]} is   ")
  #-----------------------------   For process 2 total surface area of cylinder------------------------------

      elif user[-2].lower() in  datas["61"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=cylindertotalsurfacearea(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for total surface area of cylinder with r : {a[0]} h : {a[1]} is   ")
  #-----------------------------   For process 2 total surface area of cone------------------------------

      elif user[-2].lower() in  datas["62"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=conetotalsurfacearea(int(a[0]),int(a[1]))
          return finalans(Bot,tempans,f"for total surface area of cone with r : {a[0]} l : {a[1]} is   ")
  #-----------------------------   For process 2 total surface area of sphere------------------------------

      elif user[-2].lower() in  datas["63"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=spheretotalsurfacearea(int(a[0]))
          return finalans(Bot,tempans,f"for total surface area of sphere with r : {a[0]} is   ")
  #-----------------------------   For process 2 total surface area of hemisphere------------------------------

      elif user[-2].lower() in  datas["64"][1]:
          a=user[-1].split(" ")
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          tempans=hemispheretotalsurfacearea(int(a[0]))
          return finalans(Bot,tempans,f"for total surface area of hemisphere with r : {a[0]} is   ")


#-----------------------------   For process 2 addition------------------------------

      elif user[-2].lower() in  datas["67"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          for i in a:
             tempans+=int(i)
          return finalans(Bot,tempans,f"for Addition answer of given numbers is ")

#-----------------------------   For process 2 subtraction------------------------------

      elif user[-2].lower() in  datas["68"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          for i in a:
             tempans-=int(i)
          return finalans(Bot,tempans,f"for subtraction answer of given numbers is ")
#-----------------------------   For process 2 multiplication------------------------------

      elif user[-2].lower() in  datas["69"][1]:
          a=user[-1].split(" ")
          tempans=1
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          for i in a:
             tempans*=int(i)
          return finalans(Bot,tempans,f"for multiplication answer of given numbers is ")
#-----------------------------   For process 2 Division------------------------------

      elif user[-2].lower() in  datas["70"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          
          return finalans(Bot,int(a[0])/int(a[1]),f"for Division answer of given numbers is ")
#-----------------------------   For process 2 Reminder------------------------------

      elif user[-2].lower() in  datas["71"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          
          return finalans(Bot,int(a[0])%int(a[1]),f"for Reminder answer of given numbers is ")
#-----------------------------   For process 2 Quotient------------------------------

      elif user[-2].lower() in  datas["72"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          
          return finalans(Bot,int(a[0])//int(a[1]),f"for Quotient answer of given numbers is ")
#-----------------------------   For process 2 square root------------------------------

      elif user[-2].lower() in  datas["73"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          
          return finalans(Bot,math.sqrt(int(a[0])),f"for Square Root answer of given numbers is ")
#-----------------------------   For process 2 exponent------------------------------

      elif user[-2].lower() in  datas["74"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          return finalans(Bot,int(a[0])**int(a[1]),f"for Exponent answer of given numbers is ")



#-----------------------------   For process 2 sinθ------------------------------

      elif user[-2].lower() in  datas["75"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          return finalans(Bot,math.sin(math.radians(int(a[0]))),f"for sinθ answer of given θ value is ")
#-----------------------------   For process 2 cosθ------------------------------

      elif user[-2].lower() in  datas["76"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          return finalans(Bot,math.cos(math.radians(int(a[0]))),f"for cosθ answer of given θ value is ")
#-----------------------------   For process 2 tanθ------------------------------

      elif user[-2].lower() in  datas["77"][1]:
          a=user[-1].split(" ")
          tempans=0
          for i in a :
            if i.isalpha():
              botmsg=Bot
              temp=["Oops!.Wrong input","","",""]
              botmsg.append(temp)
              return botmsg
          return finalans(Bot,math.tan(math.radians(int(a[0]))),f"for tanθ answer of given θ value is ")
      elif Bot[-1] in datas["78"][1]:
                botmsg=Bot
                botmsg.append(datas["78"][2])
                return botmsg
      
      elif ("help" in user[-1] and "ho" in user[-1]) or ("name" in user[-1]):
                botmsg=Bot
                botmsg.append(["Hello,I am bright!","","",""])
                return botmsg
      elif "ho" in user[-1] and "are" in user[-1]:
                botmsg=Bot
                botmsg.append(datas["78"][2])
                return botmsg
      elif  "love" in user[-1]:
                botmsg=Bot
                botmsg.append(["As an AI chatbot, I\'m not capable of feeling emotions or reciprocating feelings, so I don\'t experience love.","","",""])
                return botmsg
      elif  "do" in user[-1]:
                botmsg=Bot
                botmsg.append(["I am doing my best to answer your question.","","",""])
                return botmsg
      
      else:
        botmsg=Bot
        temp=["Oops!.Something went wrong","Oops!.Wrong input","Sorry,verify your input",
          "Oops!.That is not the expected input!","Something went wrong,kindly check your input",
          "Oops!Error Detected.Kindly Check your input",f"Cannot under stand this : {user[-1]}"]
        botmsg.append([random.choice(temp),"","",""])
        return botmsg
  except:
    botmsg=Bot
    temp=["Oops!.Something went wrong","Oops!.Wrong input","Sorry,verify your input",
          "Oops!.That is not the expected input!","Something went wrong,kindly check your input",
          "Oops!Error Detected.Kindly Check your input",f"Cannot under stand this : {user[-1]}"]
    botmsg.append([random.choice(temp),"","",""])
    return botmsg
  


# ["",["   For find square root of given number","Enter the values a","Example: ","a"],
#     "https://www.youtube.com/watch?v=wSBxW7LW3DA","",""]

  