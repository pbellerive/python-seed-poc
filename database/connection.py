from sqlalchemy import create_engine
from sqlalchemy.engine import URL

class Connection(object):
    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead of the constructor")

    @classmethod
    def instance(cls):
        if cls._instance == None:
            url = URL.create(
                drivername="postgresql",
                username="postgres",
                password="dev",
                host="localhost",
                database="poc_seed"
            )

            engine = create_engine(url)
            engine.connect()

            cls._instance = engine
        return cls._instance

