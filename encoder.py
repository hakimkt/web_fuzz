import base64
import sys

# Get the plain PowerShell script from the first command line argument
plain_script = sys.argv[1]

# Encode the plain script into a base64 string
encoded_script = base64.b64encode(plain_script.encode('utf-16le')).decode('utf-8')

# Print the encoded script
print(encoded_script)
