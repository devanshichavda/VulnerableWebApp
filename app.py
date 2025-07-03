from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    #print login attempt
    print(f"User tried to login with {username}:{password}")
    return redirect(url_for("home"))
  return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
