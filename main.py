from flask import Flask, render_template, Response, request
from Camera import Camera
from time import sleep
from Telegram import Telegram
# from Servo import Servo

app = Flask(__name__, static_url_path='/static')
cam = Camera()
telegram = Telegram()
# servo = Servo()
sleep(10)

@app.route('/')
def index():
    return render_template('index.html')

def sendStream():
    while True:      
        yield (b' --frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + cam.frame() + b'\r\n')

@app.route('/video')
def video():
    return Response(sendStream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/', methods=['POST'])
def controlCam():
    if request.method == 'POST':
        if request.form.get('<') == '<':
            print("Ok")
        #     servo.left()
        # elif request.form.get('>') == '>':
        #     servo.right()
        # elif request.form.get('center') == 'O':
        #     servo.center()
        elif request.form.get("picture") == '📷':
            telegram.sendFile(cam.picture(), "foto")
        elif request.form.get("record") == '🔴':
             telegram.sendFile(cam.record(30), "video")
        elif request.form.get("detect") == '👤':
            print(cam.turnDetector())
    return render_template('index.html')
        
    
app.run('0.0.0.0', port='5000', debug=False)