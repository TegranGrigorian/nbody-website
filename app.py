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

@app.route('/docs/nbody-simulation-docs')
def nbody_simulation_docs():
    return flask.render_template('docs/nbody-simulator/nbody-simulator-docs.html')

@app.route('/docs/nbody-simulator/kosmos-docs')
def kosmos_docs():
    return flask.render_template('docs/nbody-simulator/kosmos-docs.html')

@app.route('/docs/nbody-simulator/body-docs')
def body_docs():
    return flask.render_template('docs/nbody-simulator/body-docs.html')

@app.route('/docs/nbody-simulator/nbody-simulator-docs.html')
def nbody_simulator_docs():
    return flask.render_template('docs/nbody-simulator/nbody-simulator-docs.html')

@app.route('/docs/docs-option.html')
def docs_option():
    return flask.render_template('docs/docs-option.html')

if __name__ == '__main__':
    app.run(debug=True)