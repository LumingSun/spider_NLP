import urllib.request
def open_url(url):
    req=urllib.request.Request(url)
    respond=urllib.request.urlopen(req)
    html=respond.read().decode('utf-8')
    return html
list = ['baidu.com','youku.com','ruc.edu.cn','facebook.com','google.com','yahoo.com','sdfaasdf']
for each in list:
    web = 'https://www.alexa.com/siteinfo/' + each
    print(web)
    html = open_url(web)
    print(html)