from bs4 import BeautifulSoup

with open('text.html' ,'r') as f:
  data = f.read()

xml = BeautifulSoup(data, 'xml')

# print(xml)
names = xml.find_all('testsuite')
for n in names:
  print(n.text)
