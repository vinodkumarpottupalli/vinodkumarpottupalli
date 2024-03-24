from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/index", methods = ['GET'])
def getFrom():
    try:
        filename = request.args.get('name')

        return send_file(filename, as_attachment=True)
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    app.run()