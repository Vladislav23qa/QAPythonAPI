import json

string_as_json_format ='{"answer":"Hello, User"}'
obj=json.loads(string_as_json_format)

key = "answer3"
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в json нет!")