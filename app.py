from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "secret123"   # required for login

# Dummy user (for demo)
USERNAME = "admin"
PASSWORD = "1234"

expenses = []

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if user == USERNAME and pwd == PASSWORD:
            session["user"] = user
            return redirect("/dashboard")
        else:
            return "Invalid login"

    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        expense = request.form["expense"]
        amount = request.form["amount"]
        expenses.append((expense, amount))

    return render_template("dashboard.html", expenses=expenses)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
