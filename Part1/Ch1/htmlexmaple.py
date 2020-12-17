from urllib.request import urlopen

html = urlopen('http://pythonscraping.com/pages/page1.html')
# use python3 to run this progarm
print(html.read())
