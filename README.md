# selenium-google-authenticator

## Description
This is a simple Python script that uses `Selenium` + `pyotp` to automate the process of logging into a Google account with Google Authenticator enabled. It is useful for people who have multiple Google accounts and want to automate the process of logging into their Google accounts.

## Installation

Install Poetry (https://python-poetry.org/docs/#installation) and run `poetry install` in the root directory of the project.

```$ brew install poetry```

```$ poetry install```

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

