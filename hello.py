from flask import Flask, escape, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/ping')
def ping():
    return render_template('ping.html')
@app.route('/pong',methods=['GET','POST'])
def pong():
    #request.args => get방식으로 데이터가 들어올 때.
    #request.form => post방식으로 데이터가 들어올 때.
    #print(request.form.get('keyword'))
    #keyword=request.args.get('keyword')
    keyword=request.form.get('keyword')
    return render_template('pong.html',keyword=keyword)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/summoner')
def summoner():
    return render_template('summoner.html')

@app.route('/opgg')
def opgg():
    username=request.args.get('username')
    opgg_url=f"https://www.op.gg/summoner/userName={username}"
    res=requests.get(opgg_url).text
    soup=BeautifulSoup(res,'html.parser')
    tierrank=soup.find('div',{'class':'TierRank'}).text
    return render_template('opgg.html',username=username,tierrank=tierrank)

if __name__ == '__main__':
    app.run(debug=True)