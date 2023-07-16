from flask import Flask, render_template
from datetime import datetime
from functions import avions 

#"""Import of function  to the API CALL"""

app = Flask(__name__)
app.static_url_path = "/static"


@app.route("/")
def homess():
    code, rep = avions()
    return render_template('avions2.html', rep=rep, code=code)


if __name__ == '__main__':
   app.run(debug=False, host='0.0.0.0')