import requests
from datetime import datetime, timedelta

class Reddit():
    def __init__(self):
        self.refresh_token()
        
    def refresh_token(self):
        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

        data = {'grant_type': 'password',
            'username': 'netomathedi',
            'password': 'senhasenha'}

        headers = {'User-Agent': 'MyBot/0.0.1'}

        res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

        expires_in = res.json()['expires_in']

        TOKEN = res.json()['access_token']

        headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

        now = datetime.now()
        interval = timedelta(hours=1)

        valid = now + interval
        self.headers, self.valid = headers, valid
    
    def get_request(self, url):
        if self.valid < datetime.now():
            refresh_token()
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json()