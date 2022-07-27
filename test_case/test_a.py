import time

import allure


@allure.feature("我是A")
class TestA():
    @allure.story("我是test_1")
    def test_1(self):
        with allure.step("打印test_1"):
            time.sleep(1)
            print("我是test_1")

    @allure.story("我是test_2")
    def test_2(self):
        with allure.step("打印test_2"):
            time.sleep(1)
            print("我是test_2")
            assert 1==0

    @allure.story("我是test_3")
    def test_3(self):
        with allure.step("打印test_3"):
            time.sleep(1)
            print("我是test_3")
