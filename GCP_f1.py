# 這次會用到的套件
import os
import requests
import json
import hmac
import hashlib
import base64
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

line_bot_api = LineBotApi(os.environ.get('CAT'))
channel_secret = os.environ.get('CS')
UID = os.environ.get('UID')

handler = WebhookHandler(channel_secret)
url = "https://XXXX.ngrok-free.app"

def send_text(data):
    # 任意消息
    payload = {"message": data}
    response = requests.post(url, json=payload)

def linebot(request):
    if request.method == 'POST':
        if 'X-Line-Signature' not in request.headers:
            line_bot_api.push_message(UID, TextSendMessage(text='有入侵者!!!'))
            image_url_1 = 'https://storage.cloud.google.com/XXXX/XXXX.jpg'
            image_message_1 = ImageSendMessage(original_content_url=image_url_1, preview_image_url=image_url_1)
            line_bot_api.push_message(UID, image_message_1)
            #return 'Error: Invalid source', 403
        else:
            # get X-Line-Signature header value
            x_line_signature = request.headers['X-Line-Signature']
            # get body value
            body = request.get_data(as_text=True)
            # decode body
            hash = hmac.new(channel_secret.encode('utf-8'),
                        body.encode('utf-8'), hashlib.sha256).digest()
            signature = base64.b64encode(hash).decode('utf-8')
            # Compare x-line-signature request header and the signature
            if x_line_signature == signature:
                try:
                    json_data = json.loads(body)
                    handler.handle(body, x_line_signature)
                    tk = json_data['events'][0]['replyToken']         # 取得 reply token
                    msg = json_data['events'][0]['message']['text']   # 取得 訊息 
                    # 判斷訊息內容，非指定內容即回覆原文
                    if msg == 'Fire':
                        line_bot_api.reply_message(tk,TextSendMessage('Fire!!'))
                        send_text('111')
                    elif msg == 'Reset':
                        line_bot_api.reply_message(tk,TextSendMessage('Reset'))
                        send_text('000')
                    elif msg == 'Support':
                        # 上傳圖片至某個公開可訪問的位置，並將以下URL替換為實際的圖片URL
                        image_url = 'https://drive.google.com/XXXX'
                        image_message = ImageSendMessage(original_content_url=image_url, preview_image_url=image_url)
                        line_bot_api.reply_message(tk, image_message)
                    else:
                        line_bot_api.reply_message(tk,TextSendMessage(msg))
                    #line_bot_api.reply_message(tk,TextSendMessage(msg)) # 回傳 訊息
                    # print(msg, tk)
                    return 'OK', 200
                except:
                    print('error')
            else:
                return 'Invalid signature', 403
    else:
        return 'Method not allowed', 400