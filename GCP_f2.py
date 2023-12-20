import requests
import functions_framework

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def send_invasion(cloud_event):
    # webhook url
    url = "https://XXXX/HomeSecurity"
    # 任意消息
    payload = {"message": "000"}
    response = requests.post(url, data=payload)
