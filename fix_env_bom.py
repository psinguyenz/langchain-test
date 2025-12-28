# Script to remove BOM from .env file
with open('.env', 'rb') as f:
    content = f.read()

# Remove BOM if present
if content.startswith(b'\xef\xbb\xbf'):
    content = content[3:]
    with open('.env', 'wb') as f:
        f.write(content)
    print("BOM removed from .env file")
else:
    print("No BOM found in .env file")
