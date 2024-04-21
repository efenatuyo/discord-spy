import ujson as json
class spy:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = json.loads(open("data.json", "r").read())
        return cls._instance
