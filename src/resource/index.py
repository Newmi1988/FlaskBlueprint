from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

index_page = Blueprint('index', __name__, template_folder= 'templates')

@index_page.route('/', defaults = {'page' : 'index'})
@index_page.route('/<page>')
def show(page):
    try: 
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
