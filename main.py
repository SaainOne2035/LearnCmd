import pytest

class MainClass():
    class_number = 20

    def __init__(self, getLocalNumber, class_number):
        self.getLocalNumber = getLocalNumber


getClassNumber = MainClass.class_number
