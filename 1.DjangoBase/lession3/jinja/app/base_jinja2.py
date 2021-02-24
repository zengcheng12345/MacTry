#coding:utf-8

from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from .myfilter import test   # 注意加上.myfilter


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse
    })
    env.filters['test'] = test  # 将自定义的过滤器导入到主目录中；
                                # 注意是filters，不能掉s
    return env

