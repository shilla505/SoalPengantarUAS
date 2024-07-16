import json

json_string = """
[
    {"1": "one", "2": "two", "3": "three"},
    {"1": "un", "2": "deux", "3": "trois"},
    {"1": "eins", "2": "zwei", "3": "drei"}
]
"""

data = json.loads(json_string)
result = data[1]["2"]
print(result)