# -*- coding: utf-8 -*-
# @Time    : 10/7/23 8:00 PM
# @Author  : stdchi

# Load the patch
import patch
import requests

proxy = "http://usename:password@host:port"

proxies = {
    'http': proxy,
    'https': proxy,
}

res = requests.get("https://www.google.com/", proxies=proxies, verify=False)
print(res.status_code)
