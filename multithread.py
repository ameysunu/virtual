from concurrent.futures import ThreadPoolExecutor
import docker
import random


def fun(message, client):
    container = client.containers.run(
        "eon01/md5summer", environment=["var=%s" % message], detach=True)
    logs = container.logs()

    for line in container.logs(stream=True):
        print(line.strip())


client1 = docker.from_env()
messages = [
    "c4ca4238a0b923820dcc509a6f75849b",
    "c4ca4238a0b923820dcc509a6f758491",
    "c4ca4238a0b923820dcc509a6f75849c",
    "c4ca4238a0b923820dcc509a6f75849d",
    "c4ca4238a0b923820dcc509a6f75849b",
    "c4ca4238a0b923820dcc509a6f758491",
    "c4ca4238a0b923820dcc509a6f75849c",
    "c4ca4238a0b923820dcc509a6f75849d",
    "c4ca4238a0b923820dcc509a6f75849b",
    "c4ca4238a0b923820dcc509a6f758491",
    "c4ca4238a0b923820dcc509a6f75849c",
    "c4ca4238a0b923820dcc509a6f75849d"
]
pool = ThreadPoolExecutor(50)

for my_message in messages:
    future = pool.submit(fun, (my_message), client1)
