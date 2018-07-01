
class DbType(object):
    name = None
    value_type = object


class Integer(DbType):
    name = 'int'
    value_type = int


class Text(DbType):
    name = 'text'
    value_type = str


class Float(DbType):
    name = 'float'
    value_type = float


class Boolean(DbType):
    name = 'int'
    value_type = bool