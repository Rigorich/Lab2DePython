
CUR_PATH = ""
SOURCE_NAME = "SAVED_Function_Source.txt"
CODE_NAME = "SAVED_Function_Code.txt"

from serializers.function_serializers import source_function_saver, code_function_saver


def check(f):
    assert f(1)(2) == 3

def test_source():
    f = source_function_saver.function_load(CUR_PATH + SOURCE_NAME)
    check(f)

def test_code():
    f = code_function_saver.function_load(CUR_PATH + CODE_NAME)
    check(f)
