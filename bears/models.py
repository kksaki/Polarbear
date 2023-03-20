from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Bear(models.Model):
    bearID = models.IntegerField()
    pTT_ID = models.IntegerField()
    capture_lat = models.FloatField()
    capture_long = models.FloatField()
    sex = models.TextField()
    age_class = models.TextField()
    ear_applied = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    #在对象被创建时，该字段会自动设置为当前时间，而不是对象被修改时更新#


    def __str__(self):
        return self.bearID, self.pTT_ID, self.capture_lat, self.capture_long, self.sex,self.age_class, self.ear_applied, self.created_date

    def female():
        females = Bear.objects.filter(sex='F')
        return females



# class Sighting(models.Model):
#     bear_id = models.ForeignKey ('bears.Bear', on_delete = models.CASCADE, related_name='sighting') #当Bear model中的一个实例被删除时，与之关联的Sighting实例也会被删除
#     # bears.Bear代表上面的class bear表
#     #related_name是可选参数，它允许您设置反向关系的名称，从而可以通过反向关系从Bear实例中访问相关的Sighting实例。在这种情况下，反向关系将被命名为"sighting"，因此您可以使用bear.sighting.all()访问该熊的所有Sighting实例。
#     deploy_id = models.IntegerField(default=None)
#     received = models.TextField()
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     #temperature = models.FloatField()
#     created_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.bear_id}, {self.deploy_id}, {self.received}, {self.latitude}, {self.longitude}, {self.created_date}'

    # def __str__(self):
    #     return f'{self.bear_id}, {self.deploy_id}, {self.received}, {self.latitude}, {self.longitude}, {self.created_date}'