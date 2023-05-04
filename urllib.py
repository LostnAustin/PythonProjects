import urllib.request, urllliv.parse, urllib.error

#grabbing html from the web

fhand = urllib.request.urlopen('http:/www.dr-chuck.com/page1.html')
for line in fhand:
  print(line.decode().strip())
