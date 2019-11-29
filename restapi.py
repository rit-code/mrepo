#Rest Api calls
import requests
from bs4 import BeautifulSoup
#import urllib2
#import re

response = requests.get("https://www.google.co.in/")
print(response.status_code)



soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
    print()


#html_page = urllib2.urlopen("https://www.google.co.in/")
#soup = BeautifulSoup(html_page)
#for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
#    print(link.get('href'))



