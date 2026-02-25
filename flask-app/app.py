from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Week 1 Success!</title></head>
        <body>
            <h1>🚀 DevOps Journey - Week 1 Complete!</h1>
            <p>This web app is running as user: webapp</p>
            <p>Deployed manually using Linux fundamentals</p>
            <p>Owner: Juan Pablo DiGiovanni</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
