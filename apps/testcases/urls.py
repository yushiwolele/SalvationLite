from django.urls import path

from testcases.views import config_views,operation_views,script_views

app_name = 'testcases'
urlpatterns=[
    path('testcase_config/',config_views.config_list_view,name='testcase_config'),
    path('config_data/',config_views.get_all_config_file,name='config_data'),
    path('config_upload/',config_views.config_upload,name='config_upload'),
    path('config_delete_file/',config_views.config_delete_file,name='config_delete_file'),
    path('download_config_template_file/',config_views.download_config_template_file,name='download_config_template_file'),
    path('testcase_template/',config_views.template,name='testcase_template'),
    path('template_delete_file/',config_views.template_delete_file,name='template_delete_file'),
    path('related/',config_views.related,name='related'),
    #操作
    path('reuseCommonTestCases/',operation_views.reuseCommonTestCases,name='reuseCommonTestCases'),
    path('generateScript/',operation_views.generateScript,name='generateScript'),

    #脚本测试套件
    path('script_config/',script_views.script_config,name='script_config'),
    path('get_script_list/',script_views.get_script_list,name='get_script_list'),
    path('get_script_file_content/',script_views.get_script_file_content,name='get_script_file_content'),
    path('update_script_file_content/',script_views.update_script_file_content,name='update_script_file_content'),
    path('upload_script_component/',script_views.upload_script_component,name='upload_script_component'),
    path('upload_script_file_component/',script_views.upload_script_file_component,name='upload_script_file_component'),
    path('download_script_folder/',script_views.download_script_folder,name='download_script_folder'),
    path('delete_script_folder/',script_views.delete_script_folder,name='delete_script_folder'),
    #脚本基线包
    path('script_baseline/',script_views.script_baseline,name='script_baseline'),
    path('upload_script_baseline_component/',script_views.upload_script_baseline_component,name='upload_script_baseline_component'),
    path('get_script_baseline_name/', script_views.get_script_baseline_name, name='get_script_baseline_name'),
]