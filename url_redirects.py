from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World...!!'

# this will appear on http://localhost:5000/link1
@app.route('/link1')
def show_link1():
   return 'This is link 1'

# this will appear on http://localhost:5000/hello/saurabh
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

# this will appear on http://localhost:5000/blog/21
@app.route('/blog/<int:postID>/')
def show_blog(postID):
   return 'Blog Number %d' % postID

#NOTE:
#@app.route('/python/')
#Extra "/" is used at end --> Hence, using /python or /python/ returns the same output, otherwise /python/ will give 404

if __name__ == '__main__':
   app.run(debug = True)
