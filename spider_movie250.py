# -*- coding: utf-8 -*-
import scrapy
from douban.items import Movie250Item  #创建的文件夹什么名字就从xxx.items去调用


class Movie250Spider(scrapy.Spider):
    name = 'movie250'
    allowed_domains = ['douban.com']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        for info in response.css('.item'):
            item = Movie250Item()  #这句不是很懂
            item['rank'] = info.css(' em::text').extract()
            item['title'] = info.css('.pic a img::attr(alt)').extract()
            item['link'] = info.css(' .pic a::attr(href)').extract()
            item['rate'] = info.css('.star .rating_num::text').extract()
            item['quote'] = info.css('.quote .inq::text').extract()
            yield item  #  如果写的是return,就不会执行下面的翻页操作


            #  翻页
            next_page = response.css('.next a::attr(href)')
            if next_page:
                url = response.urljoin(next_page[0].extract())
                yield scrapy.Request(url, self.parse) #处理后续页面的url,一页一页处理，一边处理一边放入itempipeline中

    # 继续写个回调函数处理每个电影的信息

