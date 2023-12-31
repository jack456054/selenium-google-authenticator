# selenium-google-authenticator

## Description
This is a simple Python script that uses `Selenium` + `pyotp` to automate the process of logging into a Google account with Google Authenticator enabled. It is useful for people who have multiple Google accounts and want to automate the process of logging into their Google accounts.

## Installation
Install Poetry (https://python-poetry.org/docs/#installation) and run `poetry install` in the root directory of the project.

```$ brew install poetry```

Install Python(3.11.4) dependencies

```$ poetry install```

## Setup environment variables
Create a `.env` file in the root directory of the project and add the following variables:

```
email=[Your Google Account Email]
password=[Your Google Account Password]
otp_secret=[Your Google Authenticator Secret] # This can be found in the Google Authenticator app, which we will show you how to do later.
```

## Setup Google Authenticator
Login to your Google Account and go to the [Google Authenticator](https://myaccount.google.com/signinoptions/two-step-verification) page. Click on the `Set up` button and follow the instructions to set up Google Authenticator. Once you have set up Google Authenticator, you will be able to see your secret key. Copy the secret key and paste it into the `otp_secret` variable in the `.env` file.

![Alt text](<images/Screenshot 2023-08-08 at 6.28.35 PM.png>)
![Alt text](<images/Screenshot 2023-08-08 at 6.33.10 PM.png>)
![Alt text](<images/Screenshot 2023-08-08 at 6.34.27 PM.png>)
![Alt text](<images/Screenshot 2023-08-08 at 6.35.12 PM.png>)
![Alt text](<images/Screenshot 2023-08-08 at 6.38.47 PM.png>)

You can find you OTP secret key like:

```xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx```

Fill in the `opt_secret` variable in the `.env` file with the secret key(without withespaces), which should look like this:

```xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx```

## Run the program

```$ poetry run python main.py```

## Google Account 2FA
Google Account uses TOTP to generate one-time passwords. The secret key is stored on the server and the verification code is generated by the client. The verification code is valid for 30 seconds. The client and server must be synchronized to ensure that the verification code is valid.


## Time-based One-time Password Algorithm(TOTP)
The Time-based One-time Password Algorithm(TOTP) is an algorithm that computes a one-time password from a `shared secret key` and the `current time`. It has been adopted as Internet Engineering Task Force standard RFC 6238, is the cornerstone of Initiative For Open Authentication (OATH), and is used in a number of two-factor authentication systems(2FA). You can find `shared secret key` while you're setting up Google Account 2FA. `current time` is the time on your computer in seconds since the Unix epoch, divided by the number of seconds in the time step. The time step is usually 30 seconds. Then, hash the shared secret key with the HMAC algorithm using the SHA-1 hash function. This will produce a 20-byte digest. Then, use dynamic truncation to extract a 4-byte(32-bit) code from the digest. This is the one-time password. Finally, compute the one-time password as a 6-digit decimal integer. This will be the one-time password that you will use to log into your Google account.  You can find more information about TOTP [here](https://en.wikipedia.org/wiki/Time-based_One-time_Password_algorithm).


## References
- https://en.wikipedia.org/wiki/Time-based_One-time_Password_algorithm
- https://zh.wikipedia.org/wiki/HMAC
- https://medium.com/starbugs/totp-2fa-algorithm-in-10-mins-25acc3c35df9
- https://medium.com/@henry-chou/%E6%B7%B1%E5%85%A5%E6%B7%BA%E5%87%BA%E5%85%A9%E9%9A%8E%E6%AE%B5-2fa-%E9%A9%97%E8%AD%89-1af65be74420
- https://www.tsnien.idv.tw/Security_WebBook/chap4/4-4%20SHA-1%20%E6%BC%94%E7%AE%97%E6%B3%95.html
- https://joyofcryptography.com