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

@app.route('/unse_naver')
def unse1():
    return render_template('unse_naver.html')

@app.route('/unse_result')
def unse2():
    unse_url="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B3%84%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    res=requests.get(unse_url).text
    soup=BeautifulSoup(res,'html.parser')
    unses=soup.select('#main_pack > div.content_search.section > div > div.contents03_sub > div > ul.sign_lst > li > p')
    star_list=['물병자리','양자리','쌍둥이자리','사자자리','천칭자리','사수자리','물고기자리','황소자리','게자리','처녀자리','전갈자리','염소자리']
    unse_list=[]
    for unse in unses:
        unse_list.append(unse.text)
    star=request.args.get('star')

    for i in range(12):
        if star==star_list[i]:
            unse_result=unse_list[i].split('.')[0]
    
    return render_template('unse_result.html',star=star,unse_result=unse_result)
 
if __name__ == '__main__':
    app.run(debug=True)