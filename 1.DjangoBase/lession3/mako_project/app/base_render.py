#coding:utf-8

from mako.lookup import TemplateLookup
from django.template import RequestContext
from django.conf import settings
from django.template.context import Context
from django.http import HttpResponse


def render_to_response(request, template, data=None):

    context_instance = RequestContext(request)  # 导入实例：上下文 == 输入的内容
    path = settings.TEMPLATES[0]['DIRS'][0]
    lookup = TemplateLookup(
        directories=[path],
        output_encoding='utf-8',
        input_encoding='utf-8'
    )
    mako_template = lookup.get_template(template)

    # ----------
    if not data:
        data = {}
    # 如果不存在语境，如何设置默认值
    if context_instance:
        context_instance.update(data)
    else:
        context_instance = Context(data)

    result = {}

    for d in context_instance:
        result.update(d)

    # 前端向后端传入数据时需要的
    result['csrf_token'] = '<input type="hidden" name="csrfmiddlewaretoken" value="{0}" />'.format(request.META['CSRF_COOKIE'])
    return HttpResponse(mako_template.render(**result))

