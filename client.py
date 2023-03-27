import requests

res = requests.put("http://127.0.0.1:3000/api/students/2", {"name": "ALI", "age": 99})
print(res.json())