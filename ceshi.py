import unittest
from run import app
import json
# # 可以借助于 urllib,requeset 发送请求
# import urllib
# import requests
# 登录测试
class LoginTest(unittest.TestCase):
    # 测试用户名,密码 为空的测试方法

    def setUp(self):
        app.testing = True
        # 调用测试代码之前一定会执行
        # 初始化的代码 执行 放在这里
        self.client = app.test_client()
    def test_empty_username_password(self):
        # app 对象 内置发送请求的方式 参数一 路由,参数二,数据
        response = self.client.post('/login',data={})
        json_dict = json.loads(response.data)
        # print(json_dict)
        # 断言
        self.assertIn('errcode',json_dict,'数据格式返回错误')
        self.assertEqual(1,json_dict['errcode'],'状态码返回错误')
        # requests.post('/login')

    def test_username_password(self):
        response = self.client().post('/login', data={'uname':'xiaoming','upass':'abc'})
        json_dict = json.loads(response.data)
        # print(json_dict)
        # 断言
        self.assertIn('errcode', json_dict, '数据格式返回错误')
        self.assertEqual(2, json_dict['errcode'], '用户名或者密码不正确')


# 注册测试
# class RegisterTest(unittest.TestCase):
#     pass

# 订单 会员 购物车 模块测试

if __name__ == '__main__':
    unittest.main()