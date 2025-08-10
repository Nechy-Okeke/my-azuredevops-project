from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, DevSecOps World!</h1><p>This is a secure application.</p>'

if __name__ == '__main__':
    # Use port 5000 for local development and avoid using privileged ports like 80 without proper permissions
    app.run(host='0.0.0.0', port=5000, debug=False)
