from flask import Flask , request, render_template, redirect 
import cgi 
app = Flask(__name__)
app.config['DEBUG'] = True 


@app.route("/", methods=['GET'])
def index():
    return render_template("base.html") 
@app.route("/validate", methods = ['POST'])
def validate(): 
    error = 0
    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]


    if len(username) < 3 or len(username) > 20:
        error += 1
        username_error = "Enter Valid Username"
    if len(password) < 3 or len(password) > 20:
        error += 1
        password_error = "Enter Valid Password"
    if verify_password != password:
        error += 1
        verify_password_error = "Passwords does not match"
    if email != "":
         
        if ("@"  not in email) or("." not in email):
            error +=1
            email_error = "Enter valid email"
    if error!= 0:
        return render_template("base.html",username=username,username_error=username_error,password_error=password_error,verify_password_error=verify_password_error, email_error=email_error)
    else:
        return render_template("hello.html",username=username,password=password,verify_password=verify_password,email=email)

app.run()