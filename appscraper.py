#!/usr/bin/env python

import re
import mechanize
from bs4 import BeautifulSoup

# Change these variables to your appshopper.com login info.
APPSHOPPER_USER = 'user'
APPSHOPPER_PASS = 'pass'
# Change this variable to the total number of apps in your wishlist. I realize this could be done programmatically, but... meh.
TOTAL_APPS = 535

# That's it. Let the computer do the rest...

# Let's build a browser to log in to Appshopper with our credentials.
br = mechanize.Browser()
br.open("http://appshopper.com/login?url=/")
br.select_form(nr=0)
br.form['username'] = APPSHOPPER_USER
br.form['password'] = APPSHOPPER_PASS
br.submit()

# Here's a function to access a single page of our wishlist.
# The number passed to the url gives the starting number for app count; apps are displayed 20 at a time.
def wishlist_scrape(page):
    '''Scrapes an arbitrary page of an appshopper.com wishlist for the app name and the type of app (iOS Universal, Mac, etc.)'''
    wishpage = 'http://appshopper.com/wishlist/' + str(page)
    br.open(wishpage)
    response1 = br.response()
    soup = BeautifulSoup(response1.read())
    applist = soup.find_all('ul', 'appdetails')
    appnames = applist[0].find_all('h3')
    apptype = applist[0].find_all('nobr')
    for f, b in zip(appnames, apptype):
        print "<li>"
        print f
        print b
        print "</li>"

# Let's build some basic html.
print '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My Appshopper Wishlist</title>
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/base-min.css">
  </head>
  <body>
    <main>
    <h1>Appshopper Wishlist</h1>
    <ul>
'''

for i in range(1, TOTAL_APPS, 20):
    wishlist_scrape(i)

# OK, finish off the html
print '''
    </ul>
  </main>
  </body>
</html>
'''
