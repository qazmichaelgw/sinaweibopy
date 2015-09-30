# -*- coding: utf-8 -*-

import sys
import weibo
import webbrowser
import pymongo
import urllib2
from urllib import urlencode

APP_KEY = '1948434100'
APP_SECRET = '2800c7396e4df96e11e2f3ff5f747309'
REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html'

class API():
    def __init__(self, key, secret, redirect_url):
        self.key = key
        self.secret = secret
        self.redirect_url = redirect_url
        self.get_access_token()

    def get_access_token(self):
        api = weibo.APIClient(self.key, self.secret)
        authorize_url = api.get_authorize_url(self.redirect_url)
        print(authorize_url)
        webbrowser.open_new(authorize_url)
        code = raw_input('input the code: ')
        request = api.request_access_token(code, self.redirect_url)
        self.access_token = request.access_token
        self.expires_in = request.expires_in
        #print 'access token: ', access_token
        #print 'expire: ', expires_in
        #return access_token, expires_in

    def follow(self, fid):
        api = weibo.APIClient(self.key, self.secret, redirect_uri=self.redirect_url)
        api.set_access_token(self.access_token, self.expires_in)
        r = api.friendships.create.post(uid=fid)
        return r.friendships.friends

def get_data(access_token, expires_in):
    api = weibo.APIClient(APP_KEY, APP_SECRET, redirect_uri=REDIRECT_URL)
    api.set_access_token(access_token, expires_in)
    r = api.statuses.home_timeline.get(uid='Test1', count=1)
    print r.statuses
    return r.statuses


def save_data():
    conn = Connection()
    db = conn.tweets_db
    tweets_table = db.tweets_table
    tweets_table.ensure_index('id', unique=True)

    tweets = get_data()
    orignal_count = tweets_table.count()
    for tweet in tweets:
        tweets_table.update({'id': tweet['id']}, tweet, True)
    print 'added: ', tweets_table.count() - orignal_count

if __name__ == '__main__':
    #token, expires = get_access_token()
    #token = "2.00hLR8sC9i7rHC24f90860d90gEv1e"
    #expires = 1601103176
    #get_data(token, expires)
    #follow(token, expires, 1645673224)
    api = API(APP_KEY, APP_SECRET, REDIRECT_URL)
    api.follow(1645673224)


