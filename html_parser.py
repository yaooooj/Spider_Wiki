#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlPraser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /item/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F
        links = soup.find_all('a', href=re.compile("^(/item/)"))
        for link in links:
            if 'href'in link.attrs:
                new_url = link.attrs['href']
                new_full_url = urllib.parse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data["url"] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Android</h1>
        print("这是标题")
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data["title"] = title_node.get_text()
        print(title_node.get_text())

        # <div class="lemma-summary" label-module="lemmaSummary">
        print("这是简介")
        summary_node = soup.find('div', class_="para")
        res_data["summary"] = summary_node.get_text()
        print(summary_node.get_text())
        return res_data

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, "html.parser")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
