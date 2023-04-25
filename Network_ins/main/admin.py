from django.contrib import admin
from . import models

# Register your models here.

class ServerAdmin(admin.ModelAdmin):
    list_display=['id','make','modelName','ip_address','location','type_of_port','type_of_part','date_purchase','purchase_cost','date_of_entry',]
admin.site.register(models.Server,ServerAdmin)
class SwitchAdmin(admin.ModelAdmin):
    list_display=['id','make','modelName','ip_address','location','type_of_port','type_of_part','date_purchase','purchase_cost','date_of_entry',]
admin.site.register(models.Switch,SwitchAdmin)
class WifiAdmin(admin.ModelAdmin):
    list_display=['id','make','modelName','ip_address','location','type_of_port','type_of_part','date_purchase','purchase_cost','date_of_entry',]
admin.site.register(models.Wifi,WifiAdmin)

class VlanAdmin(admin.ModelAdmin):
    list_display=['id','make','modelName','ip_address','location','type_of_port','type_of_part','date_purchase','purchase_cost','date_of_entry',]
admin.site.register(models.Vlan,VlanAdmin)
class CamerasAdmin(admin.ModelAdmin):
    list_display=['id','make','modelName','ip_address','location','type_of_port','type_of_part','date_purchase','purchase_cost','date_of_entry',]
admin.site.register(models.Cameras,CamerasAdmin)
class BiometricAdmin(admin.ModelAdmin):
    list_display=['id','make','modelName','ip_address','location','type_of_port','type_of_part','date_purchase','purchase_cost','date_of_entry',]
admin.site.register(models.Biometric,BiometricAdmin)
