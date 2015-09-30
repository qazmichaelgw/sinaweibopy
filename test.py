from weibo import APIClient
APP_KEY = '1948434100'
APP_SECRET = '2800c7396e4df96e11e2f3ff5f747309'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url
code = raw_input("input the code:").strip()
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in
print access_token

client.set_access_token(access_token, expires_in)
