// Get TDX Token
def test_api():
  customer = "test"
  url = f"https://{customer}.teamdynamix.com/TDWebApi/api/auth/login"
  data = {
    "username": "christian",
    "password": "password123"
  }
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.post(url, json=data, headers=headers)
  print(response.text)

test_api()
