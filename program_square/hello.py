from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<num>')
def success(num):
   num = int(num)
   x = "square is " + str(num * num)
   return x

@app.route('/square',methods = ['POST'])
def login():
    n = request.form['nm']
    return redirect(url_for('success',num = n))
   

if __name__ == '__main__':
   app.run(debug = True)
