import re,requests,pyperclip
from selenium import  webdriver

def playlist_id(url):
    index=str(url).index('list=')+5
    pl_id=str(url)[index:index+34]
    return pl_id

def vid_id(url):
    vidid=str(url)[str(url).index('v=')+2:str(url).index('v=')+13]
    return vidid

def getpage(url):
    req=requests.get(url)
    return req.text

def vid_urls(html_ps,pl_id):
    ytregex=re.compile(r'watch\?v=\S+?list='+pl_id)
    url_list=ytregex.findall(html_ps)
    print(url_list)
    return url_list

def downloadlink(pg_src):
    dlregex = re.compile(r'http://subtitle.{142}')
    dlink = dlregex.findall(pg_src)
    return dlink

def get_down_url(vidid):
    down_url=r'https://keepvid.com/?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D'+str(vidid)
    return  down_url

def rem_dup(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

url=str(r'https://www.youtube.com/playlist?list=PLBDA2E52FB1EF80C9')
a=0
b=0
if 'playlist' in url:
    a=int(input('Enter the first video num'))
    b=int(input('Enter the last video num'))

down_links=''
down_ps=''
count=0
links=''
browser=webdriver.Chrome()
if 'playlist' in url:
    ytps = getpage(url)
    pl_id = str(playlist_id(url))
    vid_urls=vid_urls(str(ytps), pl_id)
    vid_urls=rem_dup(vid_urls)
    if len(vid_urls[0]) != len(vid_urls[1]):
        del vid_urls[0]
    for eachurl in vid_urls:
        count += 1
        if (count < a):
            continue
        if (count == b + 1):
            break
        #down_ps=str(getpage(get_down_url(vid_id(eachurl))))
        browser.get(get_down_url(vid_id(eachurl)))
        elem=browser.find_element_by_css_selector('#subsUrl')
        elem.click()
        #down_links=downloadlink(down_ps)
        #down_links=''.join(down_links)
        #links= links+down_links+'\n'
else:
    down_ps = str(getpage(get_down_url(vid_id(url))))
    down_links=downloadlink(down_ps)
    down_links=''.join(down_links)
    links = links + down_links + '\n'


#print(links)
#pyperclip.copy(links)



'''
subtitle=downloadlink(str(pyperclip.paste()))
print(''.join(subtitle))


content=str(pyperclip.paste())
plid=playlist_id(r'https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBbSLZjvleMwldX8jGgXV6a')
print(plid)
urls=vid_urls(content, plid)
count=0
a=1
b=11
for url in urls:
    count += 1
    if(count<a):
        continue
    if(count==b+1):
        break
    act_url = str(r'https://www.youtube.com/watch?v=') + url[9:20] + r'&list='+plid + r'&index='+str(count)
    print(act_url,count)
'''





'''
urlstring=input('enter youtube url')
print('Num of subtitles range a to b to be processed')
a=int(input('enter starting index of playlist'))
b=int(input('enter last index of playlist'))
print('entered url is '+str(urlstring)+' wirh %s videos to be processed starting from %s to %s ' % (b-a,a,b))
urlstring=urlstring[:-1]
browser=webdriver.Firefox()
for i in range(a,b+1):
'''







