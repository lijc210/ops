#coding: utf8
from django.db import models

# Create your models here.

class Server_asset(models.Model):
    ip = models.CharField(max_length=20,verbose_name='IP地址')
    hostname = models.CharField(max_length=30,verbose_name='主机名')
    minion_id = models.CharField(max_length=20,null=True,default=None,verbose_name='minion_id')
    application = models.CharField(max_length=100,verbose_name='用途')
    cpu = models.CharField(max_length=30,verbose_name='cpu型号')
    menmory = models.CharField(max_length=20,verbose_name='内存大小')
    disk = models.CharField(max_length=20,verbose_name='硬盘大小')
    position = models.CharField(max_length=30,verbose_name='服务器位置')
    remarks = models.CharField(max_length=100,null=True,default=None,verbose_name='备注')

    class Meta:
        verbose_name = '服务器资产'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)

class Network_device_asset(models.Model):
    ip = models.CharField(max_length=20,verbose_name='IP地址')
    name = models.CharField(max_length=30,verbose_name='名称')
    application = models.CharField(max_length=100,verbose_name='用途')
    position = models.CharField(max_length=30,verbose_name='位置')
    remarks = models.CharField(max_length=100,null=True,default=None,verbose_name='备注')

    class Meta:
        verbose_name = '网络设备资产'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)