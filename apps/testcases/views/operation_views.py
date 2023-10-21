# -*- coding: utf-8 -*-            
# @Author : libeijie
# @Time : 2023/9/12 14:00

import time
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import escape_uri_path
from django.http import HttpResponse
from django.http import HttpResponseServerError

from testcases.service.operation.reuseCommonTestCases_service import *
from testcases.service.operation.generateAutoTestCases_service import *

@csrf_exempt
def reuseCommonTestCases(request):
    '''
    生成测试用例
    :param request:
    :return:
    '''
    # 【备注】：期望二期做成异步
    # 获取配置好的用例excel
    file = request.FILES.get('file', None)
    file_name = file.name
    #生成用例
    result_data = ReuseCommonTestCases().create_project_test_cases(file)
    if result_data['code'] == 0:  # 生成成功
        workbook = result_data['data']
        #当前时间
        time_now = str(time.time()).replace('.','_')
        excel_file_path = 'temp_test_cases_{0}.xlsm'.format(time_now) #临时文件
        workbook.save(excel_file_path)
        with open(excel_file_path, 'rb') as processed_file:
            response = HttpResponse(processed_file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment;filename={}'.format(escape_uri_path(file_name))
        #删除临时文件
        if (os.path.exists(excel_file_path)):
            os.remove(excel_file_path)

        return response
    else: #生成失败
        return HttpResponseServerError()

@csrf_exempt
def generateScript(request):
    '''
    自动生成自动化用例，并生成zip文件下载
    :param request:
    :return:
    '''
    testcase_file = request.FILES.get('file', None) #用例文件
    system = request.POST.get('system', None)  # 系统类型
    script_baseline_id = request.POST.get('script_baseline_id', None)  # 基线包id
    gat = GenerateAutolestCases()
    result_data = gat.generate_auto_test_cases(system,testcase_file,script_baseline_id)
    if result_data['code'] == 0: #生成成功
        zip_file = result_data['data']['file']
        zip_folder_name = result_data['data']['file_name']
        # 构建HTTP响应，提供ZIP文件下载
        response = HttpResponse(zip_file.getvalue(), content_type="application/zip")
        response['Content-Disposition'] = 'attachment; filename={}.zip'.format(escape_uri_path(zip_folder_name))
        return response
    else: #生成失败
        return HttpResponseServerError()


