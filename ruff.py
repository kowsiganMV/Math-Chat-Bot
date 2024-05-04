import json

a=input("Enter the value: ")
f=open('data1.json',encoding="utf8")

datas=json.load(f)

for i in range(1,3):
  if a in datas[str(i)][1]:
    print(datas[str(i)][2])


