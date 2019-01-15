import sys
from os.path import dirname, realpath, sep
sys.path.append(dirname(realpath(__file__ + sep + '..' + sep)))

from src.twispay import Twispay

# Example code for generating a HTML form to be posted to Twispay.

# sample data contains all available parameters
# depending on order type, not all parameters are required/needed
# you need to replace `siteId` etc. with valid data
dictOrderData = {
    "siteId": 1,
    "customer": {
        "identifier": "identifier",
        "firstName": "John ",
        "lastName": "Doe",
        "country": "US",
        "state": "NY",
        "city": "New York",
        "address": "1st Street",
        "zipCode": "11222",
        "phone": "0012120000000",
        "email": "john.doe@test.com",
        "tags": [
            "customer_tag_1",
            "customer_tag_2"
        ]
    },
    "order": {
        "orderId": "external-order-id",
        "type": "recurring",
        "amount": 2194.99,
        "currency": "USD",
        "items": [
            {
                "item": "1 year subscription on site",
                "unitPrice": 34.99,
                "units": 1,
                "type": "digital",
                "code": "xyz",
                "vatPercent": 19,
                "itemDescription": "1 year subscription on site"
            },
            {
                "item": "200 tokens",
                "unitPrice": 10.75,
                "units": 200,
                "type": "digital",
                "code": "abc",
                "vatPercent": 19,
                "itemDescription": "200 tokens"
            },
            {
                "item": "discount",
                "unitPrice": 10,
                "units": 1,
                "type": "digital",
                "code": "fgh",
                "vatPercent": 19,
                "itemDescription": "discount"
            }
        ],
        "tags": [
            "tag_1",
            "tag_2"
        ],
        "intervalType": "month",
        "intervalValue": 1,
        "trialAmount": 1,
        "firstBillDate": "2020-10-02T12:00:00+00:00",
        "level3Type": "airline",
        "level3Airline": {
            "ticketNumber": "8V32EU",
            "passengerName": "John Doe",
            "flightNumber": "SQ619",
            "departureDate": "2020-02-05T14:13:00+02:00",
            "departureAirportCode": "KIX",
            "arrivalAirportCode": "OTP",
            "carrierCode": "American Airlines",
            "travelAgencyCode": "19NOV05",
            "travelAgencyName": "Elite Travel"
        }
    },
    "cardTransactionMode": "authAndCapture",
    "cardId": 1,
    "invoiceEmail": "john.doe@test.com",
    "backUrl": "http://google.com",
    "customData": {
        "key1": "value",
        "key2": "value"
    }
}

# your secret key
secretKey = "cd07b3c95dc9a0c8e9318b29bdc13b03"

print("jsonOrderData: " + str(dictOrderData))
print("secretKey: " + secretKey)

# TRUE for Twispay live site, otherwise Twispay stage will be used
twispayLive = False

# get the HTML form
base64JsonRequest = Twispay.get_base64_json_request(dictOrderData)
base64Checksum = Twispay.get_base64_checksum(dictOrderData, secretKey)
hostName = ("secure-stage.twispay.com", "secure.twispay.com")[twispayLive]
htmlForm = """<form action="https://""" + hostName + """" method="post" accept-charset="UTF-8">
    <input type="hidden" name="jsonRequest" value=\"""" + base64JsonRequest + """\">
    <input type="hidden" name="checksum" value=\"""" + base64Checksum + """\">
    <input type="submit" value="Pay">
    </form>"""

print("Generated HTML form: " + htmlForm)
