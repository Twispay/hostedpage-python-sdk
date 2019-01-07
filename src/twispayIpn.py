import sys
from twispay import Twispay
from twispaySample import TwispaySample

# normally you get the encrypted data from the HTTP request (POST/GET) in the `opensslResult` parameter
encryptedIpnResponse = TwispaySample.get_encrypted_ipn_response()

# your secret key
secretKey = TwispaySample.get_secret_key()

if len(sys.argv) == 3:
    print("Arguments provided for encrypted IPN response and secret key.")
    encryptedIpnResponse = sys.argv[1]
    secretKey = sys.argv[2]
else:
    print("No arguments provided for encrypted IPN response and secret key, using sample values!")

print("encryptedIpnResponse: " + encryptedIpnResponse)
print("secretKey: " + secretKey)

# get the JSON IPN response
jsonResponse = Twispay.decrypt_ipn_response(encryptedIpnResponse, secretKey)

print("Decrypted IPN response: " + str(jsonResponse))
