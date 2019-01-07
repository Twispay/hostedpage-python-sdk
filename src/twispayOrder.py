import sys
from twispay import Twispay
from twispaySample import TwispaySample
import json

# get the data as JSON text
jsonOrderData = TwispaySample.get_order_data()

# your secret key
secretKey = TwispaySample.get_secret_key()

if len(sys.argv) == 3:
    print("Arguments provided for JSON order data and secret key.")
    jsonOrderData = json.loads(sys.argv[1])
    secretKey = sys.argv[2]
else:
    print("No arguments provided for JSON order data and secret key, using sample values!")

print("jsonOrderData: " + str(jsonOrderData))
print("secretKey: " + secretKey)

# get the HTML form
htmlForm = Twispay.get_html_order_form(jsonOrderData, secretKey)

print("Generated HTML form: " + htmlForm)
