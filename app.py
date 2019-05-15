# Bottle
import urllib.request
from sys import argv
import bottle
from bottle import *

# Föll


@route("/")
def MainPage():
    return '<h1 style="text-align: center;">Loli Police Department</h1>'



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
# Passa að það sé til login token fyrir Google Sheets API
# ##########################################################
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

# ##########################################################
# Keyra Bottle
# ##########################################################
try:
    bottle.run(host='0.0.0.0', port=argv[1])
except IndexError:
    bottle.run(host="localhost", port=8080, reloader=True, debug=True)
