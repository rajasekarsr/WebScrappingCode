import urllib # for URL loading
from bs4 import BeautifulSoup # for HTML prasing
import urlparse #to get each url

# To get all the URL in the website to Perform searchText
def Load_all_URL (url) :
    try:
        page = urllib.urlopen( url ).read()
    except:
        return []
    urlList = []
    soup = BeautifulSoup(page, "html.parser")
    soup.prettify()
    for Hook in soup.findAll('a', href=True):
            if not 'http://' and '#' in Hook['href']:
                if urlparse.urljoin(url, Hook['href']) not in urlList:
                    urlList.append(urlparse.urljoin(url, Hook['href']))
            else:
                if Hook['href'] not in urlList:
                    urlList.append(Hook['href'])
    return urlList


# To search string in the each URL 
def spider (url, searchText) :
    flag = 0
    
    try :
        wp = urllib.urlopen(url) #opens the URL
        urlContent = wp.read() # read the HTML content
    except :
        #print 'Please check URL, Cannot load url'
        return
    
    
    # To check if the page is HTML
    if urlContent.find('<html') == -1 and urlContent.find('<HTML') == -1 :
        print 'The Page is not a html page'
        return
    
    soup = BeautifulSoup(''.join(urlContent), "html.parser")
    
    
    c = soup.findAll('script')
    for i in c :
        i.extract ()
         
    try :
        bodyText = soup.body(text = True)
    except :
        return
    text = ''.join(bodyText)
    
    if text.find(searchText) > -1 :
        flag = 1
        print 'The String "'+ searchText + '" is found in the URL  : ' + url +'\n'
    else :
        return
      
    if flag == 0 :
      print 'The given text was not found in the whole Website'


#Main_Code

#Parameters we need for the program
rooturl = 'http://www.thomsonreuters.com'
searchtext1 = 'Digi-Me Rocks!!!'
searchtext2 = 'Web Scraping is Fun'

l = Load_all_URL (rooturl)

print ('Let''s beign our search in website : ' + rooturl + '\n\n\n Sit Back, Relax !!!'+ '\n\n')

for eachURL in l :
    spider(eachURL, searchtext1)

for eachURL in l :
    spider(eachURL, searchtext2)

print ('The search for both the Strings is complete !!! Thank you !!!')
