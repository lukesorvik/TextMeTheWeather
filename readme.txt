This Python script sends weather updates for a specified area (e.g., Seattle) along with an image of the sky captured from traffic cameras. 
To use this script, create a .env file following the provided example and fill in the required variables.

Please note the following:

-The script uses Gmail to send messages. If using a different email provider, you may need to modify the code in main.py. 

-The script has been tested only with Gmail for sending messages.

-When using Gmail, you must create an app password within two-factor authentication, as using the account password directly may not work.

-The recipient of the text message will see your email address. Consider creating a new email address if you prefer not to reveal your personal email.

-You can customize the code to adjust how frequently weather updates are sent.

Instructions:

1) Create a .env file with the required variables using the provided .env_example file


2) Customize the script as needed for your use case.

3) Run the script to start receiving weather updates. (can run using included run.bat file, or compile to .exe using pyinstaller)

Note:

A Markdown file for this repository is under development and will be available in the next couple of days.

Feel free to modify the provided information to better suit your intentions or specific details about the script.


Libraries to install: 

pip install requests-html

(I believe schedule, imghdr, smtplib, and email are part of the Python standard library, but you might also need to install them)