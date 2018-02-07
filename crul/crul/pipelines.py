# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests


class CrulPipeline(object):
    def process_item(self, item, spider):
        return item


class CollectPipeline(object):
    """docstring for CollectPipeline."""

    def __init__(self):
        super(CollectPipeline, self).__init__()
        print('=' * 12 + '  Collect  ' + '=' * 12)
        print('> Collect is starting...')
        self.dirname = os.path.abspath('..') +'\\output'
        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)

    def process_item(self, item, spider):
        print('=' * 12 + '  Collect  ' + '=' * 12)
        print('> Collect is processing...')
        try:
            for i in range(len(item['src'])):
                with open(self.dirname + '\\' + item['src'][i].split('/')[-1], 'wb') as f:
                    f.write(requests.get(item['src'][i]).content)
        finally:
            print('=' * 12 + '  Collect  ' + '=' * 12)
            print('> Collect is completed...')
