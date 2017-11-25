"""MOOCSERVER_V01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# input view
from message.views import getform
from message.views import login
from message.views import getFileNames
from message.views import getHtmlFiles
from message.views import mgmt_files
from message.views import deleteFile
from message.views import openFile
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sign_up/$', getform),
    url(r'^sign_up/log_in/$', login),
    url(r'^getFileNames/$', getFileNames),
    url(r'^http-get1.html$', getHtmlFiles),
    url(r'^mgmt_files/$', mgmt_files),
    url(r'^deleteFile/$', deleteFile),
    url(r'^openFile/$', openFile),
]
