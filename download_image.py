
import requests



#requests the url and saves the image as the filename
#input: url of image, filename to save image as
#output: none
def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)