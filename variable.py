from flask import Flask
app = Flask(__name__)

@app.route('/index/<username>')
def show_user_profile(username):
    return 'User Name : %s' % username

@app.route('/index/<int:userid>')
def show_user_id(userid):
    return 'User ID : %d' % userid

if __name__ == '__main__':
    app.run()