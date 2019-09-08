from django.db import models
from django.utils.html import format_html
# Create your models here.
class Industrycommittee(models.Model):
    ID=models.AutoField("编号",primary_key=True,)
    headImg =models.ImageField("用户头像",upload_to="head_img")
    def img_data(self):
        return format_html(
            '<img src="{}" width="100px"/>',
            self.headImg.url

        )

    img_data.short_description = "头像"

    name=models.CharField("姓名",max_length=10)
    address =models.CharField("地址",max_length=50)
    number = models.CharField("手机号码",max_length=20)
    plotName=models.CharField("业委会名称",max_length=20)
    submitDate =models.DateTimeField("提交日期",auto_now_add=True)
    check = models.CharField("审核状态",max_length=10,choices = (("0","待审核"),("1","通过"), ("2","拒绝")),default=0,blank=True)
    remark = models.TextField("备注",blank=True)
    class Meta:
        verbose_name = verbose_name_plural = "业委会认证"
class Getdata(models.Model):
    data = models.CharField("资料名称",max_length=100)
    count =models.IntegerField("数量")
    price = models.CharField("价格",max_length=10)
    person = models.CharField("收货人",max_length=10)
    number =models.CharField("手机号码",max_length=20)
    address =models.TextField("收货地址")
    shipments =models.CharField("发货状态",max_length=10,choices=(("0","待发货"),("1","发货")),default=0,blank=True)

    class Meta:
        verbose_name=verbose_name_plural="资料领取"
    pass


