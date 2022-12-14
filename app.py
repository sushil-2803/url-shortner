from flask import Flask, redirect, url_for, render_template, request,session, flash
from itertools import count
from pymongo import MongoClient
app= Flask(__name__)



app.secret_key='wreyuiyhsfkdl972348v7897v9080kljvkjhgv8709HKJHG0jf'
clinet =MongoClient()

# client =
client = MongoClient('mongodb://localhost:27017/')
mydatabase = client['url_shortner']

mycollection=mydatabase['urls']

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/shorten', methods=['GET','POST'])
def short():
    if request.method=='GET':
        return render_template('method_error.html')
    else:
        code=request.form['code']
        long_url=request.form['long_url']
        
        query=mydatabase['urls'].find_one({"code":code})
        
        if query is None:
            rec={
                "long_url":long_url,
                "code":code
            }
        
            record=mydatabase['urls'].insert_one(rec)
            # new_url="https://phoneix-url-short.herokuapp.com/"+code
            new_url="127.0.0.1"+code
            return render_template('success.html',new_url=new_url)
        else:
            flash('Code is already in use Please Try Again with Different Code')
            return redirect(url_for('home'))
        
@app.route('/<string:code>')
def redirection(code):
    query=mydatabase['urls'].find_one({'code':code})
    if query is None:
        flash("NO SUCH CODE")
        return redirect(url_for('home'))
    else:
        rurl=query['long_url']
        return redirect(rurl)
    
    
