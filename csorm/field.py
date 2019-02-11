import datetime


class Field:
    def __init__(self, value_type, primary=False, model=None,
                 name=None, title=None,
                 db_name=None, db_type=None):
        self._name = name
        self._title = title or name
        self._value_type = value_type
        self._primary = primary
        self._model = model
        self._db_name = db_name
        self._db_type = db_type

    def get_model_value(self, obj):
        return obj._values.get(self._name)

    def set_model_value(self, obj, value):
        obj._values[self._name] = value

    def get_db_value(self, obj):
        return obj._values.get(self._name)

    def set_db_value(self, obj, value):
        obj._values[self._name] = value

    def cast(self, value):
        return self._value_type(value)

    @property
    def primary(self):
        return self._primary

    @property
    def name(self):
        return self._name


class FloatField(Field):
    def __init__(self, title, name=None):
        super().__init__(name=name, title=title, value_type=float)


class StringField(Field):
    def __init__(self, title, name=None):
        super().__init__(name=name, title=title, value_type=str)


class DateField(Field):
    def __init__(self, title, name=None, _format=None):
        super().__init__(name=name, title=title, value_type=datetime.date)
        self._format = _format


class FieldProperty(object):
    def __init__(self, field):
        self._field = field

    def __get__(self, obj, model):
        if obj is None:
            return self._field
        return self._field.get_model_value(obj)

    def __set__(self, obj, value):
        self._field.set_model_value(obj, value)

    def __delete__(self, obj):
        pass
