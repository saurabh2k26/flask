#A Flask application is started by calling the run() method. However, while the application is under development, it should be restarted manually for each change in the code. To avoid this inconvenience, enable debug support. The server will then reload itself if the code changes. It will also provide a useful debugger to track the errors if any, in the application.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World...!!'

if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)
