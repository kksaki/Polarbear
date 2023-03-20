from django.test import Client, TestCase
from django.urls import reverse
from bears.models import Bear

class BearViewTest(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     # 设置测试数据，这些数据是自己新加入的，并不是数据库里面的
    #     Bear.objects.create(
    #         bearID = 222,
    #         pTT_ID = 345,
    #         capture_lat = 70.87402954,
    #         capture_long = -152.5647827,
    #         sex = 'M',
    #         age_class = 'A',
    #         ear_applied = 'left',
    #     )

    #     Bear.objects.create(
    #         bearID = 223,
    #         pTT_ID = 346,
    #         capture_lat = 70.87402955,
    #         capture_long = -152.5647829,
    #         sex = 'F',
    #         age_class = 'A',
    #         ear_applied = 'left',
    #     )

    fixtures = ['bears.json']

    def test_views_uses_correct_template(self):
        response = self.client.get(reverse('bear_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'bears/bear_list.html')
#检查是否有这个模板
#reverse 是一个 Django URL 反向解析函数。它可以根据 URL 模式的名称和可选参数构建出相应的 URL 字符串。具体来说，它会接收一个视图函数的名称（或者是在 urls.py 中定义的名称），然后返回一个能够匹配该视图函数的 URL 字符串。这个函数的主要作用是在 Django 应用程序中使用可重用的 URL 模式，而不是直接使用硬编码的 URL。
    def test_index(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Polar bears Tagged for Tracking")

    def test_bear(self):
        client = Client()
        response = client.get('/bear/1/')
       # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bear:")
        self.assertContains(response, "222")

#在test_view_uses_correct_template方法中，使用了self.client，这是在测试类的setUp方法中定义的客户端，用于创建一个测试客户端并向应用程序发送请求。因此，变量response前面需要加上self，以便在整个测试类中使用该变量。

#而在test_story_text方法中，没有使用测试客户端，而是在测试方法内部创建了一个新的客户端。因此，在该测试方法中，没有必要在response前面添加self。

#总之，当在测试类的setUp方法中定义了一个客户端时，您需要使用self前缀，以便在整个测试类中使用该客户端。如果您在测试方法中创建了新的客户端，则可以直接使用变量名称，无需添加self前缀。