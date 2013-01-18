from bottle import get, post, request, run
import os

@get('/')
def index():
	return "Please visit the <a href='/login'><b>/login</b></a> page."

@get('/login')
def login_form():
    return '''<form method="POST" action="/login">
    			Name:
                <input name="name"     type="text" />
                Password:
                <input name="password" type="password" />
                <br/>
                <input type="submit" />
              </form>
              <small><i>Hint: try 'admin' and 'admin'</i></small>'''

@post('/login')
def login_submit():
    name     = request.forms.get('name')
    password = request.forms.get('password')

    if check_login(name, password):
        return "<p>Your login was correct</p>"
    else:
        return "<p>Login failed</p>"


def check_login(name, password):
	if name == "admin" and password == "admin":
		return True
	else:
		return False


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))