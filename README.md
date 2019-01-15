# Twispay sample code for Python

Sample code for generating a HTML form for a Twispay order:

```python
# sample data contains order parameters
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
        "email": "john.doe@test.com"
    },
    "order": {
        "orderId": "external-order-id",
        "type": "recurring",
        "amount": 2194.99,
        "currency": "USD",
        "description": "1 year subscription on site",
        "intervalType": "month",
        "intervalValue": 1,
        "trialAmount": 1,
        "firstBillDate": "2020-10-02T12:00:00+00:00"
    },
    "cardTransactionMode": "authAndCapture",
    "cardId": 1,
    "invoiceEmail": "john.doe@test.com",
    "backUrl": "http://google.com"
}

# your secret key
secretKey = "cd07b3c95dc9a0c8e9318b29bdc13b03"

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
```

Sample code for decrypting the Twispay IPN response:

```python
# normally you get the encrypted data from the HTTP request (POST/GET) in the `opensslResult` parameter
encryptedIpnResponse = "oUrO8wW0IXK1yj9F8RYbHw==,Hrw4AkEt+DBALL4P9gNDyBxkvnjh3wxlgAdqe1jVffEGrwpEpCKc3eYjR4l+mi9dCxPuvXRceVgqd7ypn9aXGLXejxClumv4l2Ym2djbpsi2PFRWyWXHoJar+NX8aLU/yCYdHUoNtvoZRA2RI13IUCLZZ1znlQdyEL9NXQTEAxrbZe7a4vmYbUDBosAiIfApGLGMWQG/OF+ebukvLeZGajzUbhbp69k8/UD03dT8NBDMSos5XayJNnEibM2unImh6tcOek5prenHQOqkIv7TeGfC3HQDxUgXH2Rw8j+7Kyu/p72AYTCvXrJOoAVJ00KKDXTi4xu7+a5VJwP/tpdLz5jeoIfivzgxPP9I/o72OhSrdAZcxPQ5YjbyS22IXhz7G1MkHX0ItytWRqKyfXjq+58LS2ovlQu3eYhoftfBjsq3xisdjqTld9V+DL97qCcWzHo7hscMLO7/5nrXsGiSY16PZ6tUtqe9lI4ErvC+71iH+i44NijMTXMt9uX01V/4Wqlz8m5sDE4Nl0uM31eV2M1MvLKyV1tntj78WREX/mpuqclD8wWO+weglzqfyaF/"

# your secret key
secretKey = "cd07b3c95dc9a0c8e9318b29bdc13b03"

# get the IPN response
dictResponse = Twispay.decrypt_ipn_response(encryptedIpnResponse, secretKey)
```

Run the sample code from the command line using Pipenv:

- execute `pipenv run python ./example/twispayOrder.py` to generate and output the HTML form for a Twispay order;
- execute `pipenv run python ./example/twispayIpn.py` to decrypt and output the received data from a IPN call.
