from flask import Flask, render_template

app = Flask(__name__) ##Creates a Flask app instance

@app.route('/')
def home():
    # This renders the HTML file from /templates
    return render_template('index.html')

if __name__ == '__main__':
    # debug=True lets you see errors and auto-reloads the server
    app.run(debug=True)
