
# Automated Weather Updates Via Text Messages

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

- I provide examples for Google Fi, and T-Mobile. If you want to send SMS via email through other carriers, you'll need to find out the specific email-to-SMS gateway address for each carrier you want to support. Unfortunately, there's no universal standard for this, and you may need to refer to the documentation or contact the carrier directly to obtain the correct email-to-SMS gateway address.

##  Libraries to install:

```bash
pip install requests-html
```


## Instructions:

1. Create a `.env` file with the required variables using the provided `.env_example` file.

2. Update the `city = "city you want to get weather from"` variable in `main.py` to get weather from a specific area

3. Find The URL Of The Traffic Camera to Scrape (refer to section below)

4. Customize the script as needed for your use case (update frequency of schedule at `schedule.every().day.at("09:00").do(job)` in `main.py`).

5. Run the script to start receiving weather updates. (can run using included `run.bat` file, or compile to `.exe` using pyinstaller)

## Finding The URL Of The Traffic Camera To Scrape:
1. Find local traffic cameras (I googled "seattle traffic cameras" in my case)
2. Find a camera you like, get the page to display the image from the camera
4. While hovering over the image from the camera : `Right-Click, Inspect` 
5. Find the `<img src=" THE URL HERE" > `  in the html
6. Copy the url
7. Make sure the url for the image is not static, and that the camera updates to the same url for all photos
8. Paste the url into the `main.py` in the `image_url = ""` variable
9. You are done :)


## Note:

This readme is currently a work in progress, it should be done within the next few days


