import flask

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('homepage.html')

@app.route('/install')
def install_page():
    return flask.render_template('install.html')

@app.route('/docs')
def docs_page():
    return flask.render_template('docs/docs-option.html')

if __name__ == '__main__':
    app.run(debug=True)