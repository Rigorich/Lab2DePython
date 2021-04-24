
from serializers.object_serializers.serializer import object_to_dict

from serializers.object_serializers.json_serializer import JsonSerializerCreator
from serializers.object_serializers.pickle_serializer import PickleSerializerCreator
from serializers.object_serializers.yaml_serializer import YamlSerializerCreator
from serializers.object_serializers.toml_serializer import TomlSerializerCreator


CUR_PATH = ""
FILE_EXTENSION = ".txt"


class SubObjectParent():
    def __init__(self):
        self.a = 1
        self.b = "2"
        self.c = True

class SubObject(SubObjectParent):
    def __init__(self):
        SubObjectParent.__init__(self)
        self.d = {"a": 13, "top": "kek", "SPAM": "eggs"}

class LeClass():
    num = int
    flt = float
    txt = str
    bul = bool
    arr = list
    tup = tuple
    sed = set
    dct = dict
    obj = object

    def init(self):
        self.num = 42
        self.flt = 3.1416
        self.txt = "Test de test"
        self.bul = True
        self.arr = [13, 69, 420, 0]
        self.dct = {"a": 13, "42": "13", "top": "kek", "meh": ["eggs", "SPAM"]}
        self.obj = SubObject()

    def __str__(self):
        s = ""
        s += type(self).__name__
        s += "\n"
        for (k, v) in object_to_dict(self).items():
            s += f"{k} = {v} \n"
        return s


LeObject = LeClass()
LeObject.init()
#print(LeObject)


def check_creator(creator):

    s = creator.dumps(LeObject)
    obj = creator.loads(s, LeClass)
    assert str(obj) == str(LeObject)
    
    fn = CUR_PATH + type(creator).__name__ + FILE_EXTENSION
    s = creator.dump(LeObject, fn)
    obj = creator.load(fn, LeClass)
    assert str(obj) == str(LeObject)

def test_json():
    creator = JsonSerializerCreator()
    check_creator(creator)
    
def test_pickle():
    creator = PickleSerializerCreator()
    check_creator(creator)
    
def test_yaml():
    creator = YamlSerializerCreator()
    check_creator(creator)
    
def test_toml():
    creator = TomlSerializerCreator()
    check_creator(creator)
