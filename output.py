# -*- coding: utf-8 -*-
import json


def readmoviejson():
    infile = open("C:\Users\Administrator\lpthw\douban\douban\spiders\items.json", 'r')
    text = infile.read()  # text是str
    movie_dict = json.loads(text)  # movie_dict是list
    for movie in movie_dict:  # movie是dict
        rank = movie["rank"][0]  # rank等都是Unicode
        title = movie["title"][0]
        link = movie["link"][0]
        rate = movie["rate"][0]
        if movie["quote"]:
            quote = movie["quote"][0]
        else:
            quote = u"暂无"

        # str和Unicode不能混用，要么将Unicode类型encode为其他编码。要么将str类型decode为其他编码
        # python的内部使用Unicode，str如“电影： ”是字节串，由Unicode经过编码(encode)后的字节组成的
        # 下句等价于 print "电影: " + title.encode("utf-8") + " 链接: " + link.encode("utf=8")
        res = 'top' + rank + '.' + title + u' 评分' + '(' + rate + ')' + u'\n链接：' + link +  u'\n豆瓣评论：' + quote + '\n'
        print res.encode('gbk', 'ignore')
        # print (u'top%s.%sfff（%s） link%s pl:%s' % (rank, title, rate, link, quote)).encode('gbk', 'ignore')
        #print title
        #print quote.encode('gbk', 'ignore')
        # print (u'##########暂无 %s' % quote).encode('gbk', 'ignore')

readmoviejson()


