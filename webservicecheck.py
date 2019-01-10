from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import urllib
import http.client

# pushover info
token = ''
user = ''

indata = {'servicename': 'ip/url'}


def SendPush(message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": token,
                     "user": user,
                     "message": message,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()


def checkstatus(inputkey, url):
    try:
        response = urlopen(url)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        m = str(inputkey)+' '+str(e.code)
        print(m)
        SendPush(m)

    except URLError as e:
        print('We failed to reach a server.')
        m = str(inputkey)+' : '+str(e.reason)
        print(m)
        SendPush(m)
    else:
        pass

if __name__ == "__main__":

    for x in indata:
        checkstatus(x, indata[x])
