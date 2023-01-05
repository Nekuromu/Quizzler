import requests

response = requests.get("https://opentdb.com/api.php", params={"amount": 10, "category": 15, "type": "boolean", "difficulty": "easy"})
response.raise_for_status()
question_data = response.json()["results"]
