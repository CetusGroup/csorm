from collections import OrderedDict

from csorm.field import FieldProperty


class ModelMetaClass(type):

    @classmethod
    def __prepare__(mcls, name, bases):
        return OrderedDict()

    def __new__(mcls, name, bases, attrs):
        cls = super(ModelMetaClass, mcls).__new__(mcls, name, bases, attrs)
        if cls.__name__ == 'Model':
            return cls
        cls.manager = ModelManager(cls)
        for attr_name, attr in attrs.items():
            cls.manager.add_field(attr_name, attr)
        return cls


class ModelManager:

    def __init__(self, model):
        self._model = model
        self._primary_key = None
        self._fields = OrderedDict()

    @property
    def fields(self):
        return self._fields

    def add_field(self, field_name, field):
        self._fields[field_name] = field
        field._name = field_name
        field._model = self._model
        if field.primary_key:
            self._primary_key = field
        setattr(self._model, field.name, FieldProperty(field))


class Model(metaclass=ModelMetaClass):

    def __init__(self, **values):
        self._values = values

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self._values)

    def __repr__(self) -> str:
        return self.__str__()
