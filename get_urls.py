import requests

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def format(saga, cap):
    return f'https://multimedia.xarxacatala.cat/one-piece/saga-{saga}/op_cat-{cap}.mp4'

print(exists(format(18, 155)))