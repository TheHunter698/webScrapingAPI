#Python 
#Used url http://py4e-data.dr-chuck.net/
# https://www.github.com/

import urllib.request, urllib.error, urllib.parse
import re

pyarse = dict()

def parseHTML(url):
    htmlFile = urllib.request.urlopen(url)
    
    for initialTag, initialLine in enumerate(htmlFile):
        currentTag = re.findall('^<([a-z]+)\s.+>', initialLine)
        currentIdentation = re.findall('(\s+)<')
        for finalTag, finalLine in enumerate(htmlFile):
            tag = re.findall('</'+currentTag+'>', finalLine)
            tagIdentation = re.findall('(\s+)</'+currentTag+'>')
            if len(tag) > 0 and tagIdentation[0] == currentIdentation[0]:
                #parse in object
            else:
                continue

while True:
    url = input('Insert the url you want me to see: ')

    if url == 'exit':
        break

    metaDataHandle = urllib.request.urlretrieve(url)
    metaData = dict()
    
    for key in metaDataHandle[1]:
        metaData[key] = metaDataHandle[1][key]

    contentType = re.findall('.+html.+', metaDataHandle[1]['Content-Type'])

    if len(contentType) > 0:
       print('HTML file detected, retrieved the ' + metaData['Date'] + ' parsing document.')
       parseHTML(url)
    else:
        print('Not an HTML file, parsing is not supported (yet) for this kind of file.')
        break



    
