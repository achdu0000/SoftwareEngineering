"""CET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path
from manager import views as mngr_views
from reg import views as reg_views
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     re_path(r"^$", mngr_views.hello),
#     path('test/', mngr_views.show_items, name='test'),
# ]
urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^$", mngr_views.hello),
    path('test/', mngr_views.show_items, name='test'),
    path("reg_view/", reg_views.index),
    path("reg_template_test/", reg_views.template_test),
    path("reg_main/", reg_views.reg_main),
    path('ConfirmRegState/', reg_views.ConfirmRegState, name='ConfirmRegState'),
]