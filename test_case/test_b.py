import time

import allure


@allure.feature("我是B")
class TestB():
    @allure.story("我是test_4")
    def test_1(self):
        with allure.step("打印test_4"):
            time.sleep(1)
            print("我是test_4")

    @allure.story("我是test_5")
    def test_2(self):
        with allure.step("打印test_5"):
            time.sleep(1)
            print("我是test_5")

    @allure.story("我是test_6")
    def test_3(self):
        with allure.step("打印test_6"):
            time.sleep(1)
            print("我是test_6")