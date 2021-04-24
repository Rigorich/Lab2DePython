
import inspect
#import dis
#import types
#import ctypes

returned_function_name = "function_saver_savedfunction"


def get_source_code(func: object, serialized: set) -> str:
    serialized.add(func.__name__)
    source = inspect.getsource(func)
    dump = ""
    globs = func.__globals__.copy()
    for name in globs:
        val = globs[name]
        if \
            not inspect.ismodule(val) and \
            name in source:
                if inspect.isfunction(val):
                    if not val.__name__ in serialized:
                        dump += get_source_code(val, serialized)
                else:
                    dump += name + " = " + repr(val) + '\n'
    dump += source + '\n'
    return dump
    
def function_dumps(func) -> str:
    code = get_source_code(func, set())
    code += returned_function_name + " = " + func.__name__ + '\n'
    return code

def function_dump(func, fp: str):
    f = open(fp, "w")
    f.write(function_dumps(func))
    f.close()


def function_loads(s: str) -> object:
    d = {}
    exec(s, d)
    return d[returned_function_name]

def function_load(fp: str) -> object:
    file = open(fp, "r")
    s = file.read()
    file.close()
    return function_loads(s)