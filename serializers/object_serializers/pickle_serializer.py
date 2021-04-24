
import pickle
from serializers.object_serializers.serializer import *


class PickleSerializer(ISerializer):
    
    def dumps(self, obj: object) -> str:
        return pickle.dumps(obj)
    
    def loads(self, s: str) -> object:
        return pickle.loads(s)


class PickleSerializerCreator(SerializerCreator):
    
    def create_serializer(self) -> ISerializer:
        serializer = PickleSerializer()
        return serializer
    
    def loads(self, s: str, cls=None) -> object:
        serializer = self.create_serializer()
        obj = serializer.loads(s)
        return obj
    
    def dump(self, obj: object, fp: str) -> None:
        s = self.dumps(obj)
        f = open(fp, "wb")
        f.write(s)
        f.close()
    
    def load(self, fp: str, cls=None) -> object:
        f = open(fp, "rb")
        s = f.read()
        f.close()
        obj = self.loads(s, cls)
        return obj
