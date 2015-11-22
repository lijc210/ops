from django.contrib import admin
from models import *



class Server_asset_Admin(admin.ModelAdmin):
    list_display = ('id','ip', 'hostname', 'minion_id','application','cpu','menmory','disk','position','remarks')
    list_display_links = ('id','ip', 'hostname')
    # list_editable = ()

class Network_device_asset_Admin(admin.ModelAdmin):
    list_display = ('id','ip', 'name', 'application','position','remarks')
    list_display_links = ('id','ip', 'name')
    # list_editable = ()

# Register your models here.

admin.site.register(Server_asset,Server_asset_Admin)
admin.site.register(Network_device_asset,Network_device_asset_Admin)
