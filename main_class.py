import pytest

class MainClass():
    __class_number = 20

    def __init__(self, getLocalNumber, class_number):
        self.getLocalNumber = getLocalNumber


getClassNumber = MainClass.__class_number


class MainClassTest():
    def __init__(self):
        pass


