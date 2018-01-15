#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html_downloader
import html_outputer
import html_parser
import url_manager
import urllib.error


class SpiderMain:

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlPraser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('爬取URL %d : %s' % (count, new_url))
                html_cont = self.downloader.downloader(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count > 100:
                    break
                count += 1
            except urllib.error.HTTPError as e:
                print('craw failed %s', e)
            self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/android/60243"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
