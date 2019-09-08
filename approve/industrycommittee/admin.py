from django.contrib import admin
from .models import Industrycommittee,Getdata

# Register your models here.
@admin.register(Industrycommittee)
class IndustryCommittee(admin.ModelAdmin):
    list_display = ('name','img_data','address','number','plotName','submitDate','check','remark')
    search_fields = ['name','plotName','number']
    list_filter = ['check']

    readonly_fields = ('img_data',)
# admin.site.register(Industrycommittee,IndustryCommittee)
#   --和上面装饰器的功能一样，绑定models(二选一)

@admin.register(Getdata)
class GetData(admin.ModelAdmin):
    list_display = ['data','count','price','person','number','address','shipments']
    search_fields =['person','number']
    list_filter = ['shipments']




