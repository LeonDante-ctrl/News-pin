from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting general sources
    newproduct = get_sources('general')

    print(newproduct)

    title = 'Home - Welcome to The best News-Highlight Website Online'
    return render_template('index.html', title = title, general = newproduct)
