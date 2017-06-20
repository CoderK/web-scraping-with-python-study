from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

print("### siblings")
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})

print("")
print("### images")
for image in images:
    print(image["src"])

print("")
print("### tags with two attributes")
tagsWithTwoAttrs = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in tagsWithTwoAttrs:
    print(tag)

