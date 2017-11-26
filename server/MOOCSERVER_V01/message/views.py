
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import UserMessage
import json
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
<<<<<<< HEAD
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

=======
import os, sys, platform
import posixpath
import BaseHTTPServer
from SocketServer import ThreadingMixIn
import threading
import urllib, urllib2
import cgi
import shutil
import mimetypes
import re
import time
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@csrf_exempt
def deleteFile(request):
     print 'deleteFile'
     mydeleteFile = request.POST.get('name')
     print 'deleteFilename is : ',mydeleteFile
     #遍历所有文件目录，找到名字匹配的文件
     filepath = ''
     # a = os.getcwd()
     # print 'os.getcwd(): ',a
     # print 'is dir: ', os.path.isdir(os.getcwd())
     for dirpath, dirnames, filenames in os.walk(os.getcwd()):
         for file in filenames:
             # print 'file: ', file
             if file == mydeleteFile.decode('utf-8').encode('gbk'):
                print 'dirpath is: ',dirpath
                filepath = os.path.join(dirpath, mydeleteFile)
                filepath = filepath.decode('utf-8').encode('gbk')
                # uipath = unicode(filepath , "utf8")
     print '删除文件的目录是：',filepath#返回想要删除文件的当前目录
     if os.path.exists(filepath):
        os.remove(filepath)
        dstatus = "%s 删除成功!"%(mydeleteFile)
     else:
        dstatus = "%s 文件找不到，删除失败!"%(mydeleteFile)
     return HttpResponse(str(dstatus))


@csrf_exempt
def openFile(request):
    print 'openFile'
    myopenFile = request.POST.get('name')
    print 'openFilename is : ',myopenFile
    filepath = ''
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for file in filenames:
            if file == myopenFile.decode('utf-8').encode('gbk'):
                print 'dirpath is: ',dirpath
                filepath = os.path.join(dirpath, myopenFile)
                filepath = filepath.decode('utf-8').encode('gbk')
    print '打开文件的目录是：',filepath

    return HttpResponse(filepath)









>>>>>>> 607b0c371438e27be5a25142e2a1cceb2e57eca8
@csrf_exempt
def mgmt_files(request): #列出树形目录，上传文件页面
    #if request.method == "POST";
    # print 'mgmt_files'
    # print request.method
    # if request.method == 'POST':
<<<<<<< HEAD
    path_root = "F:\\moocPro" #上传文件的主目录
    myFile = request.FILES.get("file",None) # 获取上传的文件，如果没有文件，则默认为None
    print myFile
    # print request
=======
    
    # print 'items: ', request.POST.items()
    myTpye = request.POST.get('type')#获取文件类型，单选框内容
    # print 'type is: ', request.POST.get('type')
    # myTpye = request.get("type") 
    print myTpye
    myFile = request.FILES.get("file",None) # 获取上传的文件，如果没有文件，则默认为None
    print myFile
    # print request
    path_root = os.path.join('F:\\moocPro\\server\\MOOCSERVER_V01\\files',myTpye) #上传文件的主目录
    print 'path_root: ',path_root
>>>>>>> 607b0c371438e27be5a25142e2a1cceb2e57eca8
    if not myFile:  
        dstatus = "没有上传文件!"
    else:
        # print 'nihao'
       # path_ostype = os.path.join(path_root,request.POST.get("ostype"))
        path_dst_file = os.path.join(path_root,myFile.name)
        #print path_ostype
        print path_dst_file
       # print os.path.isfile(path_dst_file)
        if os.path.isfile(path_dst_file):
            dstatus = "%s 已存在!"%(myFile.name)
            print dstatus
        else:
            destination = open(path_dst_file,'wb+')    # 打开特定的文件进行二进制的写操作  
            for chunk in myFile.chunks():      # 分块写入文件  
                destination.write(chunk)  
            destination.close()  
            dstatus = "%s 上传成功!"%(myFile.name)
    return HttpResponse(str(dstatus))

    # return render(request,'sinfors/mgmt_files.html')


def mgmt_file_download(request,*args,**kwargs): #提供文件下载页面
    #定义文件分块下载函数 
    def file_iterator(file_name, chunk_size=512):
        with open(file_name,'rb') as f: #如果不加‘rb’以二进制方式打开，文件流中遇到特殊字符会终止下载，下载下来的文件不完整
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    path_root = "F:\\moocPro"
    if kwargs['fpath'] is not None and kwargs['fname'] is not None:
        file_fpath = os.path.join(path_root,kwargs['fpath']) #kwargs['fapth']是文件的上一级目录名称
        file_dstpath = os.path.join(file_fpath,kwargs['fname']) #kwargs['fname']是文件名称

        response = StreamingHttpResponse(file_iterator(file_dstpath))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(kwargs['fname']) #此处kwargs['fname']是要下载的文件的文件名称
        return response
# Create your views here.
# 注册
def getform(request):

    if request.method == "POST":
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.password = password
        user_message.save()

    return render(request,'sign_up.html')

# 登陆
def login(request):

    return render(request, 'log_in.html')

# @csrf_exempt
# def getFileNames(request):
#     # print 'getFileNames'
#     # data = { "lists":[{"filename":'test', "filesize":'data'},
#     #                  {"filename":'test1', "filesize":'data1'},
#     #                  {"filename":'test2', "filesize":'data2'}
#     # ] }
#     # jsonData = json.dumps(data)
# return HttpResponse(jsonData, content_type="application/json")
@csrf_exempt
def getFileNames(request):
    fileNames = []
    fileSizes = []
    path1 = 'F:\moocPro\server\MOOCSERVER_V01\\files\ppt'
    
    print 'path is: ', path1
    getListFiles(path1, fileNames, fileSizes)
    print 'fileNames length is: ', len(fileNames)
    
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    for index in range(len(fileNames)):
      #print 'index is: ', index
      tempDic1 = {"filename":fileNames[index], "filesize":fileSizes[index]}
      #tempDic.get((tempDic.keys())[0])
      #(tempDic.values())[0]
      data1.append(tempDic1)

    path2 = 'F:\moocPro\server\MOOCSERVER_V01\\files\word'
    fileNames = []
    fileSizes = []
    getListFiles(path2, fileNames, fileSizes)
    # print 'fileNames is: ', fileNames
    for index in range(len(fileNames)):
      #print 'index is: ', index
      tempDic2 = {"filename":fileNames[index], "filesize":fileSizes[index]}
      #tempDic.get((tempDic.keys())[0])
      #(tempDic.values())[0]
      data2.append(tempDic2)
    # print 'data2 is: ',data2

    path3 = 'F:\moocPro\server\MOOCSERVER_V01\\files\gloss'
    fileNames = []
    fileSizes = []
    getListFiles(path3, fileNames, fileSizes)
    # print 'fileNames is: ', fileNames
    for index in range(len(fileNames)):
      #print 'index is: ', index
      tempDic3 = {"filename":fileNames[index], "filesize":fileSizes[index]}
      #tempDic.get((tempDic.keys())[0])
      #(tempDic.values())[0]
      data3.append(tempDic3)
    # print 'data2 is: ',data2

    path4 = 'F:\moocPro\server\MOOCSERVER_V01\\files\\accessibility'
    fileNames = []
    fileSizes = []
    getListFiles(path4, fileNames, fileSizes)
    # print 'fileNames is: ', fileNames
    for index in range(len(fileNames)):
      #print 'index is: ', index
      tempDic4 = {"filename":fileNames[index], "filesize":fileSizes[index]}
      #tempDic.get((tempDic.keys())[0])
      #(tempDic.values())[0]
      data4.append(tempDic4)
    # print 'data2 is: ',data2

    path5 = 'F:\moocPro\server\MOOCSERVER_V01\\files\\video'
    fileNames = []
    fileSizes = []
    getListFiles(path5, fileNames, fileSizes)
    # print 'fileNames is: ', fileNames
    for index in range(len(fileNames)):
      #print 'index is: ', index
      tempDic5 = {"filename":fileNames[index], "filesize":fileSizes[index]}
      #tempDic.get((tempDic.keys())[0])
      #(tempDic.values())[0]
      data5.append(tempDic5)
    # print 'data2 is: ',data2
    
    data = {"lists1":data1,
            "lists2":data2,
            "lists3":data3,
            "lists4":data4,
            "lists5":data5
        }

    # data = { "file":[{"filename":self.fileNames[0], "filesize":self.fileSizes[0]},
    #                  {"filename":self.fileNames[1], "filesize":self.fileSizes[1]},
    #                  {"filename":self.fileNames[2], "filesize":self.fileSizes[2]}
    # ] }
    message = json.dumps(data)
    #print type(message),message

    # self.send_response(200)
    # self.send_header('Content-type', 'application/json')
    # self.end_headers()
    # self.wfile.write(message)
    return HttpResponse(message, content_type="application/json")
  

  # fileList = []
  # fileDic = {}
  #print fileDic 
# fileNames = []
# fileSizes = []
def getListFiles(path, fileNames, fileSizes):
    for root, dirs, files in os.walk(path):  
        # fileNames = files
        for file in files: 
            print 'file name: ', file
            print 'file path :', os.path.join(path, file)
            fileNames.append(file)
            fileSizes.append(sizeof_fmt(os.path.getsize(os.path.join(path, file))))
        break

def sizeof_fmt(num):
  for x in ['bytes','KB','MB','GB']:
    if num < 1024.0:
      return "%3.1f%s" % (num, x)
    num /= 1024.0
  return "%3.1f%s" % (num, 'TB')

def translate_path(self, path):
    """Translate a /-separated PATH to the local filename syntax.
  
    Components that mean special things to the local file system
    (e.g. drive or directory names) are ignored. (XXX They should
    probably be diagnosed.)
  
    """
    # abandon query parameters
    print 'translate_path first path is: ', path
    path = path.split('?',1)[0]
    path = path.split('#',1)[0]
    path = posixpath.normpath(urllib.unquote(path))
    words = path.split('/')
    words = filter(None, words)
    path = os.getcwd()
    print 'translate_path second path is: ', path
    for word in words:
      drive, word = os.path.splitdrive(word)
      head, word = os.path.split(word)
      if word in (os.curdir, os.pardir): continue
      path = os.path.join(path, word)
    print 'translate_path path is: ', path
    print 'translate_path wuruizhu is: ', path
    return path


def getHtmlFiles(request):
    # print 'getHtmlFiles'
    # print os.getcwd()
    # print os.path.abspath('.')
    # print os.path.join('F:\moocPro\server\MOOCSERVER_V01', '\http-get1.html')
    filepath = ''
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for file in filenames:
            if os.path.splitext(file)[0] == 'http-get1':
                filepath = os.path.join(dirpath, file)

    print filepath
    f = open(filepath, 'rb')
    return HttpResponse(f.read(), content_type='text/html')

    # print os.path.realpath("http-get1.html")
    # f = open("..\http-get1.html")
    # f = open('http-get1.html', 'rb')
    # return HttpResponse(f.read(), content_type='text/html')
    # return render_to_response('http-get1.html')