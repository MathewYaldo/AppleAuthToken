
# AppleAuthToken
AppleAuthToken is a tool that dumps an Apple account's dsid and mmeAuthToken which can be used in API requests.
---

**Requirements**

1. Python 3
2. Requests (can be installed with `pip3 install requests`)

---
**How it works**

After supplying the script with an email and password, it will attempt to access an Apple API. When accessed by an account with 2FA enabled, the request will be denied and a request for a 2FA code will be sent to all of the user's devices.

After supplying the six-digit access code, the script will attempt to authenticate with the API. Since there is no paramater for a 2FA code, it can be appended to the user's password which Apple will accept.

If the six-digit 2FA code is correct, then the API responds with a plist file containing the dsid and mmeAuthToken.

**What's the purpose of a dsid and mmeAuthToken?**
A dsid:mmeAuthToken pair can be used to authenticate API requests in place of an email/password. 

**Benefits:**

 - The token can be saved and used for all future API requests.
 - Allows for authentication without 2FA.
 - Can be used in place of an email:password combination so that the password is never revealed. 
