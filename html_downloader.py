#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request

class HtmlDownLoader(object):

    def downloader(self, url):
        if url is None:
            return None
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)

        if response.getcode() != 200:
            return None
        return response.read()
