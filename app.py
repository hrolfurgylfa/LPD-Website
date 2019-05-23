# Bottle
import urllib.request
from sys import argv
import bottle
from bottle import *
import os

try:
    current_password = os.environ["current_password"]
    secret_cookie_key = os.environ["secret_cookie_key"]
except KeyError:
    current_password = "please"
    secret_cookie_key = "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"

# Föll


@route("/")
def MainPage():
    return template("main_page/main_page.tpl")

@route("/login")
def login():
    password = request.get_cookie("logged_in_LPD_database", secret=secret_cookie_key)

    if password == current_password: return redirect("/database")
    elif password is not None: response.delete_cookie("logged_in_LPD_database", secret=secret_cookie_key)

    return template("logged_in/login.tpl")

@route("/get_cookie", method="POST")
def get_cookie():
    password = request.forms.password
    if password == current_password:
        response.set_cookie("logged_in_LPD_database", current_password, secret=secret_cookie_key)
        redirect("/database")
    else:
        redirect("/login")

@route("/database")
def database():
    password = request.get_cookie("logged_in_LPD_database", secret=secret_cookie_key)

    if password == current_password: return template("logged_in/database.tpl")
    else: redirect("/login")

@route("/logout")
def logout():
    response.delete_cookie("logged_in_LPD_database", secret=secret_cookie_key)
    return redirect("/login")

@route("/about_us")
def about_us():
    return template("main_page/about_us.tpl")

#  ========================================
#  Annað
#  ========================================
# Til þess að setja inn myndir
@route("/static/<skra:path>")
def static_skrar(skra):
    return static_file(skra, root="static")

#404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða
@error(404)
def notFound(error):
    return '<h2 style="color:red;text-align: center;">This page does not exist</h2>'

# ##########################################################
# Keyra Bottle
# ##########################################################
try: bottle.run(host='0.0.0.0', port=argv[1])
except IndexError: bottle.run(host="localhost", port=8080, reloader=True, debug=True)
