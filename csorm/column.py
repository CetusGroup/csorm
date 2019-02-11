

class Column(object):
    def __init__(self, name, db_type):
        self._name = name
        self._db_type = db_type

    @property
    def name(self):
        return self._name

    @property
    def db_type(self):
        return self._db_type
