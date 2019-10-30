import os

def merge(html):
    html_source = '<html>\n<head>\n<meta charset="UTF-8">\n<meta name="Generator" content="EditPlus®">\n' \
                  '<meta name="Author" content="作者">\n<meta name="Keywords" content="关键词">\n' \
                  '<meta name="Description" content="网页描述">\n<title>网页标题</title>\n</head>\n' \
                  '<body>\n<b>\n<font size="8">     新闻热点话题     </font>\n</b>\n'
    html_source = html_source + html
    html_source = html_source + '</body>\n</html>\n'
    return html_source


def html(ddate,new_word):
    html_source = '<pre>\n{}\n</pre>\n' \
                  '<marquee direction="left" align="bottom" height="40" width="100%" onmouseout="this.start()" ' \
           'onmouseover="this.stop()" scrollamount="4" scrolldelay="0" style="font-size: 30" title="hahahahahah">' \
           '{}</marquee>\n'.format(ddate,new_word)
    return html_source

if __name__ == '__main__':
    files = os.listdir(r'D:\python\topic_detection\tdt\new_word')
    html_source = ''
    for each in files:
        path = 'D:\python\\topic_detection\\tdt\\new_word\\'+ each
        ddate = each.rstrip('.txt').lstrip('new_word_')
        new_word = open(path,'r').read()
        html_source = html_source + html(ddate,new_word)
    html_source = merge(html_source)
    with open('new_topic_test.html','w',encoding='utf-8') as f:
        f.write(html_source)