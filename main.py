import flask
from replit import web
from coun import ytb

from datetime import datetime

from app import avions """Import of function  to the API CALL"""

app = flask.Flask(__name__)
app.static_url_path = "/static"

"""Web """
@app.route("/av")
def homess():
    rep = avions()
    return flask.render_template('avions2.html', rep=rep)
 
web.run(app)

