from bs4 import BeautifulSoup
import requests
import csv

TargetUrl = 'https://www.infosecurity-magazine.com/news/' #Target URL
TargetDiv = 'webpage-item with-thumbnail' #Target Content
pageNumb = 1 #Current Page number, change to index value of page
DIVS = [] #Array of content in article
hasContent = True #loop escape

while hasContent: #while true do stuff
    source = requests.get(TargetUrl+'page-'+str(pageNumb)).text #requesting page
    soup = BeautifulSoup(source, 'lxml') #reading page

    DIVS = soup.findAll('div', class_=TargetDiv) #check for content


    def GetArts(i): #output content
        ArtURL = i.a #url to full article
        ArtImg = i.a.img #article thumbnail
        ArtDate = i.a.time #published date
        ArtHead = i.a.h3 #article title
        ArtDesc = i.p #brief description of article
        
        contents = requests.get(ArtURL['href']).text #get article page
        Scont = BeautifulSoup(contents, 'lxml') #read article page
        pars = Scont.findAll('p') #get article content

        print(ArtImg['src']) #output img href
        print(ArtDate.text) #output date
        print(ArtHead.text) #output article heading
        print(ArtDesc.text) #output description
        for i in pars: #article content loop
            if len(i.text) >= 5: #checks if paragraph is not empty
                print(i.text) #output article content
        print('') #formating purposes

    if len(DIVS) == 0: #check if page has content or is a 404
        hasContent = False #if true stop script, you have all content

    for i in DIVS: #loops through articles
        GetArts(i) #gets articles

    pageNumb += 1 #increases page number