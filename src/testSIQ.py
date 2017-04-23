import requests
import pprint

# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response.status_code)

# headers = {
#     'Accept': 'application/json',
# }

# requests.get('https://api.salesforceiq.com/v2/lists', headers=headers, auth=('$API_KEY', '$API_SECRET\n'))



headers = {
    'Accept': 'application/json',
}

params = (
    ('_start', '1'),
    ('_limit', '2'),
)

response = requests.get('https://api.salesforceiq.com/v2/lists', headers=headers, params=params, auth=('58fa79a4e4b0a9355183eb9b', 'X87mad2uRAbyEBAUcsiwROdY8kR'))

print(response.status_code)