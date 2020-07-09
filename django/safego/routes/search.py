from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf #在处理post请求的时候一定要加上
from cal_risk.cal_risk import *
from KBQA_AC.chatbot import ChatBotGraph

import logging
# 响应对象主要有三种形式：HttpResponse(),render(),redirect()
# render和redirect都是对HttpResponse的封装
# render(request,页面，字典（可选，主要传的是参数））
# redirect(页面）一般用于form表单提交，跳转到新的页面

ctx={}
handler = ChatBotGraph()

# 接收请求数据
def search_get(request):
    global ctx

    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']: #GET和POST属性都是django.http.QueryDict类的实例，这相当于dict自定义的一个类，可以单键多值

        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    ctx['rlt1']=message
    return render(request,"search_form.html",ctx)

def search_advise(request):
    global ctx
    global handler
    parameter_json = request.body
    parameter = json.loads(parameter_json)
    if parameter:
        question=parameter.get('question')
        answer = handler.chat_main(question)
        ctx['answer']=answer
        ctx['question']=question
    return HttpResponse(json.dumps(ctx), content_type="application/json,charset=utf-8")


def search_risk(request):
    global ctx
    parameter_json = request.body
    parameter = json.loads(parameter_json)
    if parameter:
        address = parameter.get('address')
        city = parameter.get('city')
        ctx['address']=address
        ctx['city']=city
        risk = cal_risk_from_name(address, city)
        strrisk=''
        if(risk==0):
            strrisk='低风险'
        elif(risk==1):
            strrisk='中风险'
        else:
            strrisk='高风险'
        ctx['risk']=strrisk
    return HttpResponse(json.dumps(ctx), content_type="application/json,charset=utf-8")

def search_simple(request):
    #处理的是用户输入的地址
    global ctx
    parameter_json = request.body
    parameter = json.loads(parameter_json)
    print(parameter)
    if parameter:
        address = parameter.get('address')
        ctx['address']=address
        city='北京'
        risk = cal_risk_from_name(address, city)
        answer = handler.chat_main(address+'防控建议')
        ctx['answer']=answer
        strrisk = ''
        if (risk == 0):
            strrisk = '低风险'
        elif (risk == 1):
            strrisk = '中风险'
        elif (risk == 2):
            strrisk = '高风险'
        else:
            strrisk = '查询不到,请检查输入的地址！'
        ctx['risk'] = strrisk
    return HttpResponse(json.dumps(ctx), content_type="application/json,charset=utf-8")

def search_detail(request):
    global ctx
    parameter_json = request.body
    parameter = json.loads(parameter_json)
    print(parameter)
    if parameter:
        lnglat = parameter.get('lnglat')
        detail_address = parameter.get('detail_address')
        ctx['detail_address'] = detail_address
        ctx['lnglat']=lnglat
        city = '北京'
        real_address=detail_address.split('市')[-1]
        print(real_address)
        risk = cal_risk_from_name(real_address, city)
        answer = handler.chat_main(detail_address+'防控建议')
        ctx['answer'] = answer
        strrisk = ''
        if (risk == 0):
            strrisk = '低风险'
        elif (risk == 1):
            strrisk = '中风险'
        elif(risk==2):
            strrisk = '高风险'
        else:
            strrisk='查询不到,请检查输入的地址！'
        ctx['risk'] = strrisk
    return HttpResponse(json.dumps(ctx), content_type="application/json,charset=utf-8")








