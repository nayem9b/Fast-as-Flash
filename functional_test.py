 import requests

ENDPOINT = "http://localhost:8000/items"

# Create item "rock" without providing quantity
r = requests.post(ENDPOINT, json={"name": "rock"})
assert r.status_code == ____
assert r.json()["message"] == "Added rock to items."

# Verify that item "rock" has quantity 0
r = requests.get(ENDPOINT + "?____=____")
assert r.status_code == 200
assert r.json()["quantity"] == 0

# Update item "rock" with quantity 100
r = requests.put(ENDPOINT, json={"name": "rock", "quantity": 100})
assert r.status_code == 200
assert r.json()["message"] == "Updated rock."

# Verify that item "rock" has quantity 100
r = requests.get(ENDPOINT + "?name=rock")
assert r.status_code == 200
assert r.json()["quantity"] == ____

# Delete item "rock"
r = requests.delete(ENDPOINT, json={____: ____})
assert r.status_code == 200
assert r.json()["message"] == "Deleted rock."

# Verify that item "rock" does not exist
r = requests.get(ENDPOINT + "?name=rock")
assert r.status_code == ____

print("Test complete.")