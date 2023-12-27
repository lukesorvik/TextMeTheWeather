from requests_html import HTMLSession

#defined globally if you want to format the output using scraper.temp or scraper.temp_unit or scraper.weather
temp = ''
temp_unit = ''
weather = ''

#input: name of city to get weather for
#output: string of weather info
def getWeather(query):
    global temp, temp_unit, weather  # Use the global keyword to refer to global variables

    s = HTMLSession()
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' })
    temp = r.html.find('span#wob_tm', first=True).text
    temp_unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text
    #uses the div class since the span class is not unique
    #chain the search to find the div class = vk_bk.wob-unit then find the span class = wob_tm
    
    
    weather = r.html.find('div.VQF4g', first = True).find('span#wob_dc', first = True).text
    return (f"The weather in {query} is {weather} {temp} {temp_unit} ")

#used for testing
#s = getWeather("seattle")
#print(s)