customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])


customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("birthdate"))


customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("birthdate", "Jan 1 1980"))


customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Fisher"
customer["birthdate"] = "Jan 1 1992"
print(customer["name"])
print(customer["birthdate"])