from csorm.db import Db


class SQLiteDb(Db):
    def __init__(self):
        super().__init__()
