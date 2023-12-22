# 自宅警備員
# 1.關於專案
透過樹莓派、PIR感應器及相機模組，建構一智能監控系統。當PIR偵測到入侵者，系統立即拍攝照片，並透過LINE機器人將警報及照片通知使用者。進一步，使用者可透過LINE指令觸發兵乓球發射機制，以增進家居安全感。

# 2.專案緣起
從熱門影片《屍速列車》《殭屍校園》等可知，未來我們可能會碰到生化實驗室病毒外洩導致喪屍橫行的情況，因此必須未雨綢繆，建立一套防衛家園的安全機制，本專案整合硬體和軟體技術，提供一個創新的居家安全監控解決方案，專案概念原型如下圖：     
![image](https://github.com/bot132298/IOT/assets/142957874/2152395e-199c-4596-98d7-e424af2cd147)

# 3.專案構想
在使用強大的防禦武器前，我們先使用安全的方式做PORTOTYPE。將市面上已有的乒乓球發射裝置、LINE bot、PIR偵測、拍照模組，此四者做整合應用。

# 4.硬體需求  
>1. 樹莓派（Raspberry Pi 3）  
>2. PIR（被動紅外線）感應器  
>3. 相機模組  
>4. L298N
>5. 直流馬達+輪子 *2 
>6. 伺服馬達(SG90)  
>7. 電池盒(3號電池 *4)

# 5.架構  
<img src="https://github.com/bot132298/IOT/assets/142957874/a33aaeca-7c80-44cd-a38c-c3a027c69eb8" alt="IOT_架構" width="700"/>

# 6.建置步驟  
>Step1.建立LINE Official Account及GCP Cloud Functions  
>[LINE 聊天機器人 - 手把手教學，輕鬆學會模仿與互動的功能 on GCP Cloud Functions](https://medium.com/@chiehwen0926/line-%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA-%E8%BC%95%E9%AC%86%E6%A8%A1%E4%BB%BF%E8%88%87%E4%BA%92%E5%8B%95%E7%9A%84%E7%B5%82%E6%A5%B5%E6%8C%87%E5%8D%97-gcp-cloud-functions-%E6%87%89%E7%94%A8%E5%AF%A6%E4%BE%8B-d4f43db3ca67)
  
  
>Step2.硬體製作  
><img src="https://github.com/bot132298/IOT/assets/142957874/afe92a61-da33-49b0-ab8b-a1f77b125294" alt="IOT_架構" width="700"/>
  
  
>Step3.設定GCP storage，當Camera拍的照片上傳時觸發Cloud Functions
>  
>Step4.利用ngrok來架server，讓LINE可以控制pi  
>[ngrok 的設定，來架一個臨時伺服器！](https://askie.today/ngrok-localhost-server-settings/)

# 7.實物照
1.完整照片  
<img src="https://github.com/bot132298/IOT/assets/142957874/1742e6bb-61ee-431e-b7d3-3a5e31cb5811" alt="IOT" width="700"/>  
2.發射器俯視圖  
<img src="https://github.com/bot132298/IOT/assets/142957874/43d05af0-226a-4532-9ed5-c6c4986a0dbf" alt="shooter" width="700"/>  
3.Pi接線圖(詳見程式碼HomeSecurity.py & Pir_Cam_Upload.py)  
<img src="https://github.com/bot132298/IOT/assets/142957874/58f04d37-75b0-4ea6-8614-c8af9d483db8" alt="pi" width="700"/>  
4.LINE畫面  
<img src="https://github.com/bot132298/IOT/assets/142957874/fdfcb188-e99f-47ff-be96-bed803b1499f" alt="LINE" width="400"/>  
5.發射影片  
[![YouTube 預覽圖片](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=b9Vw9VESqFI)  


# 8.參考資料
>1.ChatGPT(程式碼主要來源)  
>2.LINE Chatbot  
>https://medium.com/%E8%BB%9F%E9%AB%94%E9%96%8B%E7%99%BC/google-cloud-function-%E9%81%8B%E7%87%9F-line-bot-71ac13b2b01a  
>3.乒乓球發射器  
>https://www.youtube.com/watch?v=gtUIb_-7HC4  
>4.L298N模組教學  
>https://emmanuel-studios.blogspot.com/2020/02/l298n-rototics-by-sam-arduino-20200205.html  
>5.Ngrok
>https://askie.today/ngrok-localhost-server-settings/
