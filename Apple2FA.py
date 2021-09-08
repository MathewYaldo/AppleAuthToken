import requests
import base64
import plistlib



def PromptForVerification(email, password):

    headers = {
        'Host': 'p49-buy.itunes.apple.com',
        'Accept': '*/*',
        'User-Agent': 'iTunes-iPhone/5.1.1 (6; 16GB; dt:73)',
        'X-Apple-Client-Application': 'Software',
        'X-Apple-Client-Versions': 'iBooks/2.1.1; iTunesU/1.1.1; GameCenter/2.0',
        'X-Apple-Connection-Type': 'WiFi',
        'X-Apple-Store-Front': '',
    }

    params = (
        ('appleId', email),
        ('rmp', '0'),
        ('password', password),
        ('attempt', '0'),
        ('accountKind', '0'),
        ('guid', '3a829522-ec7f-4de5-a9dc-47509d518ea9'),
        ('createSession', 'true'),
        ('why', 'signin'),
    )

    response = requests.get('https://p49-buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/authenticate', headers=headers, params=params)
    content = response.content
    pl = plistlib.loads(content)

    if response.status_code != 200:
        raise Exception('An error occured with the request. Please ensure that your credentials are correct.')
    elif "customerMessage" in pl:
        if (pl["customerMessage"] == "Your Apple ID or password is incorrect."):
            raise Exception('Invalid Apple ID & Password')
        elif (pl["customerMessage"] == "An unknown error has occurred"):
            raise Exception('Account does not appear to have 2FA enabled')
    else:
        print("Request for six-digit 2FA code sent to devices.")



def Request(email, password, code):

    info = email+":"+password+code
    auth = base64.b64encode(info.encode('utf-8')).decode("utf-8")

    headers = {
        'Host': 'setup.icloud.com',
        'Accept': '*/*',
        'Content-Type': 'application/xml',
        'Authorization': 'Basic '+auth
    }

    response = requests.get('https://setup.icloud.com/setup/authenticate/$APPLE_ID$,', headers=headers)
    content = response.content
    if response.status_code == 401:
        raise Exception('Invalid six-digit 2FA code.')
    else:
        pl = plistlib.loads(content)
        dsid = pl["appleAccountInfo"]["dsid"]
        mmeAuthToken = pl["tokens"]["mmeAuthToken"]
        return dsid+":"+mmeAuthToken




if __name__ == "__main__":

    email     = input("Email: ")
    password  = input("Password: ")
    PromptForVerification(email, password)
    code = input("Six-digit code: ")
    print(Request(email, password, code))