import pytest
from main import *

def testGetClassString():
    assert "hello" in getClassString or "Hello" in getClassString, "Не найдено ни одной из указанных подстрок"



