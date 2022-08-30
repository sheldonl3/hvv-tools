import json

import requests

# ip信誉查看：使用微步的ip_reputation api

url = "https://api.threatbook.cn/v3/scene/ip_reputation"

query = {
    "apikey": "4e879c44c2784d56821e23845576488efa184c049b0144e99df3ce36496b1e34",
    "resource": "115.171.63.157"  # 目标ip
}

response = requests.request("GET", url, params=query)

res = json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))

print(res)
