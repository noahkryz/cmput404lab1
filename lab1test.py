import requests

print(requests.__version__)

# google = requests.get("https://www.google.com")
# print(google)

var = requests.get("https://raw.githubusercontent.com/noahkryz/cmput404lab1/master/lab1test.py")
print(var.content)