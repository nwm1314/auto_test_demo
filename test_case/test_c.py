import time

import allure


@allure.feature("我是C")
class TestC():
    @allure.story("我是test_7")
    def test_1(self):
        with allure.step("打印test_7"):
            time.sleep(1)
            print("我是test_7")

    @allure.story("我是test_8")
    def test_2(self):
        with allure.step("打印test_8"):
            time.sleep(1)
            print("我是test_8")

    @allure.story("我是test_9")
    def test_3(self):
        with allure.step("打印test_9"):
            time.sleep(1)
            print("我是test_9")