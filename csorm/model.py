from collections import OrderedDict

from csorm.field import Field, FieldProperty


class ModelMetaClass(type):
    @classmethod
    def __prepare__(mcls, name, bases):
        return OrderedDict()

    def __new__(mcls, name, bases, attrs):
        cls = super(ModelMetaClass, mcls).__new__(mcls, name, bases, attrs)
        if cls.__name__ == 'Model':
            return cls
        for attr_name, attr in attrs.items():
            cls.add_field(attr_name, attr)
        return cls


class Model(metaclass=ModelMetaClass):
    _primary_key = None
    _fields = OrderedDict()

    def __init__(self, **values):
        self._values = values

    @classmethod
    def fields(cls):
        return cls._fields

    @classmethod
    def add_field(cls, field_name, field):
        cls._fields[field_name] = field
        field._name = field_name
        field._model = cls
        if field.primary_key:
            cls._primary_key = field
        setattr(cls, field._name, FieldProperty(field))

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self._values)

    def __repr__(self) -> str:
        return self.__str__()
