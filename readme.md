
# Automated Weather Updates via Text Messages

This Python script sends weather updates for a specified area (e.g., Seattle) along with an image of the sky captured from traffic cameras. 
The current schedule is to text the receipeint everyday at 9am as long as the program is running, this schedule and frequency can be edited as you like.
To use this script, create a `.env` file following the provided example and fill in the required variables. Run the program using the run.bat file

<p float="left">
  <img src="/assets/example1.jpg?raw=true" height="250">
 <img src="/assets/example2.jpg?raw=true" height="250">
</p>



## Important Notes:

- The script uses Gmail to send messages. If using a different email provider, you may need to modify the code in `main.py`.
  
- The script has been tested only with Gmail for sending messages.

- When using Gmail, you must create an app password within two-factor authentication, as using the account password directly may not work.

- The recipient of the text message will see your email address. Consider creating a new email address if you prefer not to reveal your personal email.

- You can customize the code to adjust how frequently weather updates are sent.

##  Libraries to install:

```bash
pip install requests-html
```


## Instructions:

1. Create a `.env` file with the required variables using the provided `.env_example` file.

2. Customize the script as needed for your use case.

3. Run the script to start receiving weather updates. (can run using included `run.bat` file, or compile to `.exe` using pyinstaller)

## Note:

This readme is currently a work in progress, it should be done within the next few days


