import requests

def urlShortener(url,api_key):

    headers = {
        'Authorization': f'{api_key}',
        'Content-Type': 'application/json',
    }

    data = {
        "long_url":  url,
    }

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers,json=data)
    if response.status_code == 200:
        return response.json()['link']
    else:
        print("Error Occurred/")
userInput = input("Enter Long URL: ")
API_KEY = '2d8be0107b2a40b093b39d4394b0891a7f1fc770'
shortenedLink = urlShortener(userInput ,API_KEY)
print(shortenedLink)