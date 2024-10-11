from datetime import datetime
from flask importe Flask, render_template
from flask bootstrap import bootstrap
from flask_moment import moment

app = Flask(__name__)

bootstrap = bootstrap(app)
moment = moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)    
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/')
    def index():
        return render_template("index.html", current)