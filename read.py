import gzip
import json


def read():
    with open('./symptoms-and-conditions.json.gz', 'rb') as file:
        return json.loads(gzip.decompress(file.read())
