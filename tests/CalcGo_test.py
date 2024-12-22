import requests, random

def make_expression():
    return f"{random.randint(0, 99)} {['+', '-', '*', '/'][random.randint(0, 3)]} {random.randint(0, 99)}"

url = "http://localhost:8000/api/v1/calculate"
data_list = []
for i in range(10):
    data_list.append({"expression": make_expression()})
headers = {'Content-Type': 'application/json'}
for i in range(len(data_list)):
    response = requests.post(url, json=data_list[i], headers=headers)
    print(f"{data_list[i]['expression']} = {response.json()['result']}")
