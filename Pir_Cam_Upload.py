import RPi.GPIO as GPIO
import time
import requests
import os
from picamera import PiCamera
from google.cloud import storage

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor

# 初始化相機
camera = PiCamera()

# 設定儲存路徑
save_path = "/home/pi/Pictures/"

def take_photo():
  photo_name = "photo.jpeg"
  photo_path = os.path.join(save_path, photo_name)
  camera.capture(photo_path)


# 指定你的服務帳號密鑰文件路徑
credentials_path = '/home/pi/Key/XXXX.json'

# 創建storage 客户端時指定 credentials
storage_client = storage.Client.from_service_account_json(credentials_path)

# 上傳函數
def upload_image_to_storage(bucket_name, image_path, destination_blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    if blob.exists():
        blob.delete()  # 如果同名文件存在，先删除

    blob.upload_from_filename(image_path)  # 上传新文件


#GPIO.cleanup()
while True:
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        time.sleep(2)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        take_photo()
        time.sleep(1)
        camera.close()
        upload_image_to_storage("XXXX", "/home/pi/Pictures/photo.jpeg", "uploaded-image.jpg")
        #time.sleep(2)
        break
