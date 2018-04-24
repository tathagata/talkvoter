<<<<<<< HEAD
from flask import Flask, render_template

=======
from flask import Flask
from .resources import api_bp
>>>>>>> upstream/master

application = Flask(__name__)


<<<<<<< HEAD
@application.route("/")
def hello():
    return "Hello World!"
=======
# register the API views
application.register_blueprint(
    api_bp,
    url_prefix="")
>>>>>>> upstream/master


# Run the main loop
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
