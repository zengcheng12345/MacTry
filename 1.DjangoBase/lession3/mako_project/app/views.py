#coding:utf-8

from django.views.generic import View   # 面向对象模式generic
from .base_render import render_to_response


class Test(View):
    TEMPLATE = 'test.html'

    def get(self, request):

        data = {'name': 'dewei', 'age': 30}

        print(dir())
        v
        return render_to_response(request, self.TEMPLATE, data=data)