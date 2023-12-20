from flask import Flask, request
from gpiozero import Servo, Motor
from time import sleep

def reset():
    servo = Servo(12)
    servo.min()
    sleep(2)
    
def fire():
  servo = Servo(12)
  servo.max() 

  # 定義motor
  motor1 = Motor(forward=18, backward=17)
  motor2 = Motor(forward=23, backward=22)

  # 馬達啟動
  motor1.forward()
  motor2.forward()

  # 運轉
  sleep(3)

  # close
  servo.min()
  sleep(2)


app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post_request():
    
    data = request.get_json()

    if 'message' in data:
        if data['message'] == '111':
            print('Fire')
            fire()
            return ''
        elif data['message'] == '000':
            print('Reset')
            reset()
            return ''
    
    return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run(host='0.0.0.0')

