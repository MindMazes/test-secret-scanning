// Get TDX Token
customer = "test"
url = f"https://{customer}.teamdynamix.com/TDWebApi/api/auth/login"
data = {
  aws_access_key_id: "christian",
  aws_secret_access_key: "password123"
}
headers = {
  'Content-Type': 'application/json'
}
response = requests.post(url, json=data, headers=headers)
print(response.text)
