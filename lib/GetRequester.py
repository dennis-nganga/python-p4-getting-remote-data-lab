import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        json_data = None
        try:
            json_data = json.loads(response_body)
        except json.JSONDecodeError:
            print("Error: Failed to parse JSON response.")
        return json_data
    
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)
json_data = requester.load_json()
print(json_data)