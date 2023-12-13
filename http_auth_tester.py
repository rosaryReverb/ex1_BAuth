import base64
import requests

# Kysy käyttäjänimi ja salasana
username = input("Enter username: ")
password = input("Enter password: ")

# Enkoodaa käyttäjänimi ja salasana
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# Lähetä GET-pyyntö
response = requests.get(
    "https://postman-echo.com/basic-auth",
    headers={"Authorization": f"Basic {encoded_credentials}"}
)

# Tulosta vastaus
print(response.text)
