#coding: utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from models import *
import json
import types
# Import salt modules
import salt.client
import salt.config
import salt.runner
import salt.key

# Create your views here.

#import MySQLdb
# Create MySQL connect
# conn = MySQLdb.connect(host=__opts__['mysql.host'], user=__opts__['mysql.user'], passwd=__opts__['mysql.pass'], db=__opts__['mysql.db'], port=__opts__['mysql.port'])
# cursor = conn.cursor()

master_opts = salt.config.client_config('/etc/salt/master')

def global_setting(request):
    SITE_URL = settings.SITE_URL
    #nodegroups
    nodegroups = master_opts['nodegroups']
    #所有minion分组
    group_list = []
    for group,group_value in nodegroups.items():
        group_list.append(group)
    #salt-key
    key = salt.key.Key(master_opts)
    keys = key.list_keys()
    #所有已经认证的key（list）
    minions = keys['minions']
    #file_roots
    file_roots = master_opts['file_roots']['base'][0] + '/'
    return locals()



def key():
    key = salt.key.Key(master_opts)
    keys = key.list_keys()
    #所有已经认证的key（list）
    minions = keys['minions']


def getconfig():
    pass


#首页
def index(request):
    return render(request,'index.html',locals())

#命令执行
def saltcmd(request):
    return render(request, "saltcmd.html",locals())

#日志查看
def saltlog(request):
    with open('/usr/local/test.txt') as f:
        liens = len(f.readlines())
        startlien = 0 if liens - 100 <= 0 else liens - 100
    with open('/usr/local/test.txt') as f:
        print f.readlines()[startlien:liens]
    return render(request,'saltlog.html',locals())

def saltscript(request):
    return render(request,'saltscript.html',locals())

def saltscp(request):
    return render(request,'saltscp.html',locals())

#cmd.run
def cmd(request):
    if request.method == "GET":
        #cmd.run
        tgt = request.GET.get('tgt',None)
        fun = request.GET.get('fun',None)
        arg =  request.GET.get('arg',None)
        timeout = request.GET.get('timeout',None)
        expr_form = request.GET.get('expr_form',None)
        gzip = request.GET.get('gzip',None)
        if fun in ('cmd.script','cp.get_file','cp,get_dir'):
            arg = 'salt://' + arg
        if None not in (tgt, fun, expr_form):
            cli = salt.client.LocalClient()
            if arg == '' or arg is None:
                ret = cli.cmd(tgt,fun,[],timeout,expr_form)
            else:
                #把接受到的字符串以逗号分割，生成list
                arg = arg.split(',')
                ret = cli.cmd(tgt,fun,arg,timeout,expr_form,kwarg={'gzip':gzip,'makedirs':'True'})
                for id,idval in ret.items():
                    #如果id的value是dict，转换成str
                    if type(idval) is types.DictType:
                        newval = ''
                        for k,v in idval.items():
                            newval += str(k) +':' + str(v)+'\n'
                        ret[id]=newval
    return HttpResponse(json.dumps(ret), content_type="application/json")

#minion状态
def status(request):
    if request.method == "GET":
        #salt-run
        saltrun = request.GET.get('saltrun',None)
        if saltrun != None:
            runner = salt.runner.RunnerClient(master_opts)
            ret = runner.cmd(saltrun, [])
    return HttpResponse(json.dumps(ret), content_type="application/json")


#服务器资产
def server_asset(request):
    server_asset_list = Server_asset.objects.all()
    return render(request, 'server_asset.html',locals())

#网络设备资产
def network_device_asset(request):
    network_device_list = Network_device_asset.objects.all()
    return render(request, 'network_device_asset.html',locals())