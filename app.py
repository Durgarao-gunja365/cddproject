from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Flask Docker App</title>
        <style>
            body {
                background-color: #f0f8ff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            h1 {
                color: #2c3e50;
                font-size: 3em;
                margin-bottom: 10px;
            }
            p {
                color: #555;
                font-size: 1.2em;
            }
            .box {
                background-color: #fff;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Hello from Flask App in Docker!</h1>
            <p>This Python Flask application is running inside a Docker container 🚀</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
