from threading import Thread
from recorder import Recorder
from flask import Flask, Response
from config import host, port

app = Flask(__name__)
    
def getStream():
    while True:
        yield (b'--frame\r\n\r\n' + Recorder.frame)


@app.route('/stream', methods=['GET'])
def stream():
    return Response(getStream(),mimetype='multipart/x-mixed-replace; boundary=frame'), 200

thread = Thread(target=Recorder.captureScreen)
thread.start()

if __name__ == "__main__":
    app.run(host=host, port=port)