import requests
from datetime import datetime, timedelta
import os

class Reddit():
    def __init__(self):
        self.refresh_token()
        
    def refresh_token(self):
        auth = requests.auth.HTTPBasicAuth(os.getenv('CLIENT_ID'), os.getenv('SECRET_KEY'))

        data = {'grant_type': 'password',
            'username': os.getenv('USERNAME'),
            'password': os.getenv('PASSWORD')}

        headers = {'User-Agent': 'MyBot/0.0.1'}
        print(headers)
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

        #expires_in = res.json()['expires_in']

        TOKEN = res.json()['access_token']

        headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

        now = datetime.now()
        interval = timedelta(hours=1)

        valid = now + interval
        self.headers, self.valid = headers, valid
    

    def get_request(self, url, limit=25):
        if self.valid < datetime.now():
            refresh_token()
        res = requests.get(url, headers=self.headers, params={"limit"= limit, "before" , "after"})
        if res.status_code == 200:
            return res.json()


if __name__ == '__main__':
  reddit = Reddit()
  print(reddit.get_request('https://oauth.reddit.com/api/v1/me'))
