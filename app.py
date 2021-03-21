import Results as r
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
@app.route('/index.html')
def index():
   return render_template('index.html')

@app.route('/blog.html')
def blog():
   return render_template('blog.html')

@app.route('/projects.html')
def projects():
   return render_template('projects.html')

@app.route('/stock')
def stocks():
  return render_template('stocks.html')

@app.route('/results', methods = ['POST'])
def result():
   # company_name = request.form('company_name')
   # stock_price = r.GetStockPrice('AAPL', '2021-1-14', '2021-1-14')
   return render_template('result.html')


if __name__=='__main__':
    app.run(debug= True)
    

