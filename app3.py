from flask import Flask,render_template,request
import os
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



app.add_url_rule('/home','home',home)
if __name__=='__main__':
    app.run(debug=True)