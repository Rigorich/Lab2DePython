from serializers.object_serializers import serializer

from serializers.object_serializers import json_serializer
from serializers.object_serializers import pickle_serializer
from serializers.object_serializers import toml_serializer
from serializers.object_serializers import yaml_serializer


def get_creator(extension: str) -> serializer.SerializerCreator:
    if extension == 'json':
        return json_serializer.JsonSerializerCreator()
    if extension == 'pickle':
        return pickle_serializer.PickleSerializerCreator()
    if extension == 'toml':
        return toml_serializer.TomlSerializerCreator()
    if extension == 'yaml':
        return yaml_serializer.YamlSerializerCreator()
    raise ValueError('Unknown extension: ' + extension)
