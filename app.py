from flask import Flask, request
from views import views




app = Flask(__name__)

app.register_blueprint(views, url_prefix="/views")




if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)
