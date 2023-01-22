import requests

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def format(saga, cap):
    cap_3nums = ''
    if cap < 10: cap_3nums = '00' + str(cap)
    elif cap < 100: cap_3nums = '0' + str(cap)
    elif cap < 1000: cap_3nums = str(cap)

    return f'https://multimedia.xarxacatala.cat/one-piece/saga-{saga}/op_cat-{cap_3nums}.mp4'

saga = 1
cap = 1

while cap < 1000:
    cap_exists = exists(format(saga, cap))
    if cap_exists: print(format(saga, cap))

    if not cap_exists: saga += 1
    else: cap += 1