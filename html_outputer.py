#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if self.datas is None:
            return
        self.datas.append(data)

    def output_html(self):
        f_out = open('output.html', 'w', encoding='utf-8')

        f_out.write("<html>")
        f_out.write("<body>")
        f_out.write("<table>")
        # ascii
        for data in self.datas:
            f_out.write("<tr>")
            f_out.write("<td>%s</td>" % data['url'])
            f_out.write("<td>%s</td>" % data['title'])
            f_out.write("<td>%s</td>" % data['summary'])
            f_out.write("</tr>")
        f_out.write("</table>")
        f_out.write("</body>")
        f_out.write("</html>")

        f_out.close()
