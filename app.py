# Bottle
import urllib.request
from sys import argv
import bottle
from bottle import *

# Föll


@route("/")
def MainPage():
    return template("MainPage/index.tpl")

@route("/login")
def login():
    return "<h1>Login website</h1>"

@route("/about_us")
def about_us():
    return template("about_us/index.tpl")

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
    return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'

# ##########################################################
# Keyra Bottle
# ##########################################################
try: bottle.run(host='0.0.0.0', port=argv[1])
except IndexError: bottle.run(host="localhost", port=8080, reloader=True, debug=True)
