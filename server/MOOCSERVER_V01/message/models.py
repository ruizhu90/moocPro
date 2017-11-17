#  coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserMessage(models.Model):
    name = models.CharField(max_length = 20, verbose_name= u"用户名")
    password = models.CharField(max_length = 50, verbose_name= u"密码")
    identity = models.CharField(max_length = 20, verbose_name= u"身份")

    class Meta:
        verbose_name = u"用户登陆信息"
        verbose_name_plural = verbose_name
