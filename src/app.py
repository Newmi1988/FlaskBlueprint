from flask import Flask
from src.resource.index import index_page


app = Flask(__name__)
app.register_blueprint(index_page)