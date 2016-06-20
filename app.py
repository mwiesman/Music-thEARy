from flask import Flask, render_template, session

# from extensions import mysql
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Register the controllers
app.register_blueprint(controllers.main, url_prefix='/theary', static_url_path="static")
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Listen on external IPs
# For us, listen to port 3005 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3005, debug=True)
