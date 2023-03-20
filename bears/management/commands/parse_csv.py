import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from bears.models import Bear

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # 从表中删除数据，这样，如果我们重新运行文件，就不会重复数值了
        Bear.objects.all().delete()
        print("table dropped successfully")

        # create table again
        # open the file to read it into the database
            # 获取项目根目录的路径。
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        #打开CSV文件。
        with open(str(base_dir) + '/bears/PolarBear_Telemetry_southernBeaufortSea_2009_2011/USGS_WC_eartag_deployments_2009-2011.csv', newline='') as f:

            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line

            for row in reader:
                print(row)
                bear = Bear.objects.create(
                bearID = int(row[0]),
                pTT_ID = int(row[1]),
                capture_lat = float(row[6]),
                capture_long = float(row[7]),
                sex = row[9],
                age_class = row[10],
                ear_applied = row[11],
                )
                bear.save()

        print("data parsed successfully")


        # base_dir = Path(__file__).resolve().parent.parent.parent.parent
        # with open(str(base_dir) + '/bears/PolarBear_Telemetry_southernBeaufortSea_2009_2011/USGS_WC_eartags_output_files_2009-2011-Status.csv', newline='') as f:
        #     reader = csv.reader(f, delimiter=",")
        #     next(reader) # skip the header line

        #     for row in reader:
        #         print(row)

        #         if row[4] is not '':
        #             bear_temp = row[0]
        #             print(bear_temp)
        #             bear = Bear.objects.filter(bearID = bear_temp).first()
        #             print(bear.id) #这里的id哪儿来的？？？
        #             #如果第四行不是空的：
        #             #将变量bear_temp设置为第一行的值
        #             # 打印bear_temp的值
        #             # 通过使用Bear.objects.filter（）方法从数据库中获取具有与bear_temp相同的bearID的熊对象
        #             # 打印获取的熊对象的id属性值

        #             #在 Django 中，每个模型都有一个“Manager”对象，它允许您执行数据库查询。当您创建一个新的模型时，Django会自动为该模型生成一个默认的Manager对象。这个默认Manager称为objects。也就是说，objects是Django模型的默认管理器，它允许我们对数据库执行查询。

        #             sighting = Sighting.objects.create(

        #                 deploy_id = int(row[0]),
        #                 bear_id = int(bear), #这个bear是哪个？？？
        #                 received = row[2],
        #                 latitude = float(row[4]),
        #                 longitude = float(row[5]),
        #                 #temperature = float(row[9]),
        #             )
        #             sighting.save()
        #         else:
        #             next(reader)

        #     print("data parsed successfully")