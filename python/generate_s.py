import re

with open("self_producing.py", "r") as f:
    data = f.read()

res = re.search("\'\n", data)
if res:
    # print(res.span())
    print(data[res.start()+1:].__repr__())
