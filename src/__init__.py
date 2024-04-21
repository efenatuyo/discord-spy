import ujson as json
class spy:
    data: dict = json.loads(open("data.json", "r").read())
    