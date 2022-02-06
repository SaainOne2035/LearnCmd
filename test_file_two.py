import pytest
from main2 import *

def testGetClassString():
    assert "hello" in getClassString or "Hello" in getClassString, "Не найдено ни одной из указанных подстрок"



