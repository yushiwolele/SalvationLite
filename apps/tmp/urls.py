# -*- coding: utf-8 -*-
# @File: urls.py
# @Author: HanWenLu
# @E-mail: wenlupay@163.com
# @Time: 2021/8/12  17:17

from django.urls import path

from tmp.views.tmp_views import *


urlpatterns = [
    path('enviroment_bianliang/', TmpListView.as_view(), name='enviroment_bianliang'),  # 项目列表
    path('zidingyi_bianliang/', ZidingyiBianLiangListView.as_view(), name='zidingyi_bianliang'),  # 项目列表
    path('yonglimuban/', YonglimubanView.as_view(), name='yonglimuban'),  # 项目列表
    path('yonglixiangqing/', YonglixiangqingView.as_view(), name='yonglixiangqing'),  # 项目列表
    path('shengchengyongli/', ShengchengyongliView.as_view(), name='shengchengyongli'),  # 项目列表
    path('addyongli/', AddyongliView.as_view(), name='addyongli'),  # 项目列表

]
