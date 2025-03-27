// Get TDX Token
customer = "test"
url = f"https://{customer}.teamdynamix.com/TDWebApi/api/auth/login"
data = {
  "username": "christian",
  "azure_sql_password": "password123"
}
headers = {
  'Content-Type': 'application/json'
}
response = requests.post(url, json=data, headers=headers)
print(response.text)
