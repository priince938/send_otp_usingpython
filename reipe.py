import requests
import json
import random
def send_otp(mobile,otp):
    url='https://www.fast2sms.com/dev/bulk'
    params={
        'authorization':'U63CV7LacWtShR9njPeHpNxsmdwEf2FgyvioMJTz4qDrAGb1BOJfiSdtwHq39KmMh4PgXEas8I1j7keG',
        'sender_id':'FSTSMS',
        'message':otp,
        'language':'english',
        'route':'p',
        'numbers':mobile
    }
    response=requests.get(url,params=params)
    dic=response.json()
    print(dic)
# otp generator
def genrator(mobile):
    mob = mobile

    x = []
    for i in range(9):
        tmp = mob % 10
        mob = mob // 10
        x.append(tmp)
    y1 = random.choice(x)
    y2 = random.choice(x)
    y3 = random.choice(x)
    y1, y2, y3 = y1 ** 2, y2 ** 2, y3 ** 2
    otp = str(y1 + y2 + y3)
    if len(otp) == 4:
        otp = int(otp)
        return(otp)
    elif len(otp) == 2:
        x1=str(random.choice(x))
        x2=str(random.choice(x))
        return( x1 + otp + x2 )

    elif len(otp) == 3:
        x1=str(random.choice(x))
        return(otp + x1)
    else:
        return(otp % 1000)

mobile=int(input('Enter your mobile no.'))
generate=genrator(mobile)
message='Your otp is ' + generate
send_otp(mobile,message)
