from flask import Flask, render_template, request,url_for,redirect,flash,send_from_directory
import os
from os import environ


app = Flask(__name__)

@app.route('/')
def chat():
    return render_template('chat.html')

#
#@app.route('/login',methods=['GET','POST'])
#def login():
#    userIpAddress = request.access_route[0]
#    authorizedIpAddress = environ.get('ADMIN_IP_ADDRESS')
#
#    if userIpAddress == authorizedIpAddress:
#        form = LoginForm(request.form)
#        if request.method == "POST" and form.validate():
#            if(request.form.get('username') == environ.get('ADMIN_USERNAME') and request.form.get('password') == environ.get('ADMIN_PASSWORD')):
#                return render_template('admin.html')
#            else:
#                print(form.errors)
#        else:
#            print(form.errors)
#        return render_template('login.html',form = form)
#    else:
#         return redirect(url_for('/'))


if __name__ == '__main__':
    app.config['SECRET_KEY'] = '12312312312'
    app.run(threaded=True)

