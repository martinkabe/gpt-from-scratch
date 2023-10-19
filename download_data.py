import urllib3

url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
path = "data/input.txt"

http = urllib3.PoolManager()
r = http.request('GET', url, preload_content=False)

with open(path, 'wb') as out:
    while True:
        data = r.read(500)
        if not data:
            break
        out.write(data)

r.release_conn()