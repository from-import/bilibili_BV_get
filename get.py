import requests
import urllib.parse

def get_bv_number(short_url):
    response = requests.get(short_url, allow_redirects=True)
    long_url = response.url
    print(f"Redirected URL: {long_url}")  # print out the redirected URL for debugging
    parsed_url = urllib.parse.urlparse(long_url)
    bv_number = parsed_url.path.split('/')[2]
    return bv_number[2:]  # remove the first two characters "BV"

short_url = 'https://b23.tv/gEqh9UZ'
bv_number = get_bv_number(short_url)
print(f"The number of the video is: {bv_number}")
