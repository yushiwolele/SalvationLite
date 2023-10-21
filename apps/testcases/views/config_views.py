# --*-- coding:UTF-8 --*--
# @Author : libeijie
# @Time : 2023/9/4 10:00

import json
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,FileResponse
from django.utils.encoding import escape_uri_path
from django.shortcuts import render
from django.http import HttpResponseServerError

from testcases.service.case.config_service import ConfigService


def get_all_config_file(request):
    '''
    获取用例配置文件的名称和路径
    :param request:
    :return:
    '''
    #通过service查询数据库获取
    parameters = json.loads(request.body.decode('utf8'))
    tags = parameters.get('tags')#0-配置文件；1-模板文件
    config_list = ConfigService().get_config_file(tags)
    json_data = {'code':200,'data':config_list}
    return JsonResponse(json_data)


def config_list_view(request):
    '''
    跳转至配置文件列表页
    :param request:
    :return:
    '''
    response = render(request, template_name='testcases/case_config.html', context={})
    return response

@csrf_exempt
def config_upload(request):
    '''
    上传或者更新配置文件
    :param request:
    :return:
    '''
    upload_file = request.FILES.get('file', None)
    insert_update_flag = request.POST.get('insert_update_flag', None)  # 对文件的操作0-插入；1-更新
    template_name = request.POST.get('template_name', None)  #模板文件更新操作需上传文件名字
    config_service_obj = ConfigService()
    tags = request.POST.get('tags', '0')  # 0-配置文件；1-模板文件
    #data_uuid = uuid.uuid4()
    if tags == '0':
        upload_file_type = request.POST.get('file_type', None)
        result_msg = config_service_obj.upload_config_file(upload_file, upload_file_type, int(insert_update_flag), tags)
    else:
        upload_file_type = 'TEMPLATE'
        result_msg = config_service_obj.upload_template_file(upload_file, upload_file_type, int(insert_update_flag), tags,template_name)
    return JsonResponse(result_msg)

def download_config_template_file(request):
    '''
    下载文件
    :param request:
    :return:
    '''
    tags = request.GET.get('tags', '0') #文件标识，0-配置文件，1-模板文件
    if tags == '0':
        config_flag = request.GET.get('config_type', None) #模板type
    else:
        config_flag = request.GET.get('config_name', None) #文件名字

    file_path,file_name=ConfigService().download_config_file(config_flag,tags)
    if file_path:
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Type'] = 'application/octet-stream'# 二进制文件
        response['Content-Disposition'] = 'attachment; filename={}'.format(escape_uri_path(file_name))
        return response
    else:
        return HttpResponseServerError()


def template(request):
    '''
    模板文件展示
    :param request:
    :return:
    '''
    # 通过service查询数据库获取
    response = render(request, template_name='testcases/case_template.html', context={})
    return response

def template_delete_file(request):
    '''
    根据唯一标识删除用例模板文件
    :param request:
    :return:
    '''
    parameters = json.loads(request.body.decode('utf8'))
    unique = parameters.get('unique')
    result = ConfigService().delete_template_testcase(unique)
    return JsonResponse(result)


def config_delete_file(request):
    '''
    根据唯一标识删除用例配置文件
    :param request:
    :return:
    '''
    parameters = json.loads(request.body.decode('utf8'))
    config_type = parameters.get('config_type')
    result = ConfigService().delete_config_testcase(config_type)
    return JsonResponse(result)


def related(request):
    '''
    获取db配置文件数据并跳转至配置文件列表页
    :param request:
    :return:
    '''
    # 通过service查询数据库获取
    response = render(request,template_name='testcases/related.html',context={})
    return response

# 功能全量维护 -归档
# 公共用例 - 配置文件





