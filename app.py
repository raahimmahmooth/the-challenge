import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database
users = {
    'antonio': {
        'password': 'admin123',#weakpassword
        'flag': 'THM{weak_authentication_flag}'
    },
    'user1': {
        'password': 'password',
        'flag': ''
    },
    'raahim':{
        'password': '11:2003:22',
        'flag':'THM{try_to_find_me}'
    }

}

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            if users[username]['password'] == password:
                flag = users[username]['flag']
                return f"<h2>Welcome, {username}!</h2><p>Your flag: <strong>{flag}</strong></p>"
            else:
                error = 'Incorrect password.'
        else:
            error = 'Username not found.'

    return render_template('login.html', error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)