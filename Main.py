from flask import Flask,render_template, request,redirect,url_for,flash
from workout import Bot
import datetime

app=Flask(__name__)


app.config['SECRET_KEY']='1068d00e3aaf112b3c097f72b6756887'

#------------------------speach process--------------------


#-------------------------user msg bot msg data base-----
user=[" "," "]
Botans=[" "," "]
time=[" "," "]
flashss=1

@app.route("/",methods=['POST','GET'])
def Home():
  global user,Botans,time,flashss
  if flashss==1:
    flash(f'welcome to our math chatbot','success')
  if request.form.get('action')=='send':
    user.append(request.form['usermsg'])
    Botans=Bot(user,Botans)
    tempdate=str(datetime.datetime.now())
    print(tempdate)
    for i in range(len(tempdate)):
        if tempdate[i]==" ":
          time.append(tempdate[i:-7])
          break
    return redirect(url_for('Home'))
  flashss+=1
  return render_template("Home.html",time=time,username="User",user=user,bot=Botans,length=len(user))





if __name__=='__main__':
  app.run(debug=True)