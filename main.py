
import imghdr
import smtplib
from email.message import EmailMessage

#imports so we can make it run everyday at 9am
import time
import schedule

#import the other python files we made
import scraper
import download_image

#imports environment variables from .env file
#so we can use the email and password without hardcoding it
from dotenv import load_dotenv

#so we can use the environment variables
import os

# Load environment variables from .env file
load_dotenv()

#declares variables from environment variables
SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD')
RECIPIENT_PHONE_NUMBER = os.environ.get('RECIPIENT_PHONE_NUMBER')

# URL of the image to scrape, in this case traffic cam
image_url = "https://www.seattle.gov/trafficcams/images/Latona_NE_50_EW.jpg"

city = "seattle" #city to get weather for


#function to send the text message
def send_sms(message):
    server = smtplib.SMTP('smtp.gmail.com', 587) #creates new smtplib object
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD) #logs into the email using the environment variables
    
    msg = EmailMessage() #creates new EmailMessage object
    msg.set_content(message) #sets the content of the message to the message we want to send
    msg['From'] = SENDER_EMAIL #sets the sender of the message to the email we want to send from
    msg['To'] = RECIPIENT_PHONE_NUMBER #sets the recipient of the message to the phone number we want to send to

    #gets data from the image so we can attach to the message
    with open("traffic_cam.jpg", 'rb') as picture:
        file_data = picture.read() #reads the image data
        file_type = imghdr.what(picture.name) #gets the file type of the image
        file_name = picture.name #gets the file name of the image


    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name) #adds the image as an attachment to the message
    server.send_message(msg) #sends the complete message
    server.quit() #quits the server
    print("SMS sent successfully!")


#main function that will call scraper.py to get weather data and download_image.py to get image data
def job():
    weather_info = scraper.getWeather(city) #.getWeather(city) returns a string of the weather info based on the city you inputed from scraper.py
    print(scraper.temp) #can access the temperature variable from scraper.py if you want to format the output of the message in your own way
    print(weather_info) #prints the weather info we got from scraper.py
    messageToSend = f"Good morning! {weather_info}"
    print(messageToSend) #prints the message we will send
    download_image.download_image(image_url, "traffic_cam.jpg") #download_image.py downloads the image using the url, saves it as traffic_cam.jpg
    send_sms(messageToSend)


#for testing .env variables, uncomment job() to test the text message without having to wait until 9am
job()

# Schedule the job to run every day at 9 AM
schedule.every().day.at("09:00").do(job)


while True:
    #print(f"time until next job {schedule.idle_seconds() / 3600} hours") #prints the time until the next job in hours
    print(f"sleeping... for {schedule.idle_seconds()} seconds")
    schedule.run_pending() #runs the job if we are at the scheduled time
    time.sleep(1) #sleeps for 1 second if we are not at the scheduled time