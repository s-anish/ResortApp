import hashlib

# Define a string to hash
string_to_hash = "emily"

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the string
hash_object.update(string_to_hash.encode())

# Get the hexadecimal digest of the hash
hash_hex = hash_object.hexdigest()

# Print the hash value
print(hash_hex)
