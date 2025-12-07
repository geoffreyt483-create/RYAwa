from flask import Blueprint, render_template, request, redirect, session

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == "admin@example.com" and password == "1234":
            session["user"] = email
            return redirect("/dashboard")
        else:
            return "Invalid login"

    return render_template("login.html")
