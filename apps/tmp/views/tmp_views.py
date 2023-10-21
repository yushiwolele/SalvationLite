# -*- coding: utf-8 -*-
# @File: dev_viesw.py
# @Author: HanWenLu
# @E-mail: wenlupay@163.com
# @Time: 2021/9/2  15:09

# 部署信息视图 类

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.paginator import Paginator
from project.forms.dev_from import DevCreateForm,DevUpdateForm
from project.models import DeployInfo

from util.loginmixin import LoginMixin


class TmpListView(LoginMixin, ListView):
    """
    项目部署信息列表 视图
    """
    model = DeployInfo
    context_object_name = 'project_dev'
    template_name = "tmp/enviroment_bianliang.html"
    search_value = ""
    order_field = "-prjalias"
    created_by = ''
    pagenum = 5  # 每页分页数据条数

class ZidingyiBianLiangListView(LoginMixin, ListView):
    """
    项目部署信息列表 视图
    """
    model = DeployInfo
    context_object_name = 'project_dev'
    template_name = "tmp/zidingyibianliang_list.html"
    search_value = ""
    order_field = "-prjalias"
    created_by = ''
    pagenum = 5  # 每页分页数据条数

class YonglimubanView(LoginMixin, ListView):
    model = DeployInfo
    context_object_name = 'project_dev'
    template_name = "tmp/yonglimuban.html"
    search_value = ""
    order_field = "-prjalias"
    created_by = ''
    pagenum = 5  # 每页分页数据条数

class YonglixiangqingView(LoginMixin, ListView):
    model = DeployInfo
    context_object_name = 'project_dev'
    template_name = "tmp/yonglixiangqing.html"
    search_value = ""
    order_field = "-prjalias"
    created_by = ''
    pagenum = 5  # 每页分页数据条数

class ShengchengyongliView(LoginMixin, ListView):
    model = DeployInfo
    context_object_name = 'project_dev'
    template_name = "tmp/shengchengyongli.html"
    search_value = ""
    order_field = "-prjalias"
    created_by = ''
    pagenum = 5  # 每页分页数据条数

class AddyongliView(LoginMixin, ListView):
    model = DeployInfo
    context_object_name = 'project_dev'
    template_name = "tmp/yonglixiangqing2.html"
    search_value = ""
    order_field = "-prjalias"
    created_by = ''
    pagenum = 5  # 每页分页数据条数


class TmpCreateView(LoginMixin, CreateView):
    """
    添加环境 视图
    """
    model = DeployInfo
    form_class = DevCreateForm
    template_name = "project_manage/dev/dev_add.html"

    def get_form_kwargs(self):
        # Ensure the current `request` is provided to ProjectCreateForm.
        kwargs = super(TmpCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

class TmpUpdateView(LoginMixin, UpdateView):
    """
    更新项目
    """
    model = DeployInfo
    form_class = DevUpdateForm
    template_name = "project_manage/dev/dev_update.html"




class TmpDeleteView(LoginMixin, DeleteView):
    """
    删除项目
    """
    #template_name_suffix='_delete'
    template_name = "project_manage/dev/dev_delete.html"
    model = DeployInfo
    success_url = reverse_lazy('devlist')
