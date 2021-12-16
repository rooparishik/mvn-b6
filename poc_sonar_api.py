import requests
from requests.auth import HTTPBasicAuth
token = 'token'
PARAM = {'component': 'mvn-poc', 'metrickeys': 'ncloc,complexity,violations'}
test_url = 'http://34.211.190.58:9000/api/measures/component'
test_response = requests.get(test_url,auth=HTTPBasicAuth(username=token, password=""), verify=False,params=PARAM)
test_json = test_response.json()
print(test_json)
