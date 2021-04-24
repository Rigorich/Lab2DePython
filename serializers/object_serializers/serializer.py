def object_to_dict(obj):
    if not hasattr(obj, '__dict__'):
        return obj
    dct = {}
    for elem in vars(obj):
        dct[elem] = object_to_dict(getattr(obj, elem))
    return dct


def dict_to_object(dct, cls):
    obj = cls()
    for elem in dct:
        setattr(obj, elem, dct[elem])
    return obj


class ISerializer:
    def dumps(self, obj: object) -> str:
        raise NotImplementedError

    def loads(self, s: str) -> object:
        raise NotImplementedError


class SerializerCreator:

    def create_serializer(self) -> ISerializer:
        raise NotImplementedError

    def dumps(self, obj: object) -> str:
        serializer = self.create_serializer()
        s = serializer.dumps(obj)
        return s

    def loads(self, s: str, cls=None) -> object:
        serializer = self.create_serializer()
        dct = serializer.loads(s)
        if cls is not None:
            return dict_to_object(dct, cls)
        else:
            return dct

    def dump(self, obj: object, fp: str) -> None:
        s = self.dumps(obj)
        f = open(fp, "w")
        f.write(s)
        f.close()

    def load(self, fp: str, cls=None) -> object:
        f = open(fp, "r")
        s = f.read()
        f.close()
        obj = self.loads(s, cls)
        return obj
