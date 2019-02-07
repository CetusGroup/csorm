import datetime
from typing import NamedTuple


class DbType(NamedTuple):
    name = None
    synonyms = None
    value_type = object


class SMALLINT(DbType):
    name = 'SMALLINT'
    value_type = int


class INTEGER(DbType):
    name = 'INTEGER'
    synonyms = ('INT', )
    value_type = int


class DECIMAL(DbType):
    name = 'DECIMAL'
    value_type = int
    precision = None
    scale = None


class NUMERIC(DbType):
    name = 'NUMERIC'
    value_type = int
    precision = None
    scale = None


class FLOAT(DbType):
    name = 'FLOAT'
    value_type = float
    precision = None


class DOUBLE_PRECISION(DbType):
    name = 'DOUBLE PRECISION'
    value_type = float
    precision = None


class REAL(DbType):
    name = 'REAL'
    value_type = float
    precision = None


class VARCHAR(DbType):
    name = 'VARCHAR'
    synonyms = ('CHAR', )
    value_type = str


class BOOLEAN(DbType):
    name = 'BOOLEAN'
    value_type = bool


class TIMESTAMP(DbType):
    name = 'TIMESTAMP'
    value_type = datetime.datetime


class DATE(DbType):
    name = 'DATE'
    value_type = datetime.date


class TIME(DbType):
    name = 'TIME'
    value_type = datetime.time


class TIME_WITH_TIME_ZONE(DbType):
    name = 'TIME WITH TIME ZONE'
    value_type = datetime.time
