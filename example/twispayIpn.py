import sys
from os.path import dirname, realpath, sep
sys.path.append(dirname(realpath(__file__ + sep + '..' + sep)))

from src.twispay import Twispay

# Example code for decrypting a Twispay IPN response.

# normally you get the encrypted data from the HTTP request (POST/GET) in the `opensslResult` parameter
encryptedIpnResponse = "oUrO8wW0IXK1yj9F8RYbHw==,Hrw4AkEt+DBALL4P9gNDyBxkvnjh3wxlgAdqe1jVffEGrwpEpCKc3eYjR4l+mi9dCxPuvXRceVgqd7ypn9aXGLXejxClumv4l2Ym2djbpsi2PFRWyWXHoJar+NX8aLU/yCYdHUoNtvoZRA2RI13IUCLZZ1znlQdyEL9NXQTEAxrbZe7a4vmYbUDBosAiIfApGLGMWQG/OF+ebukvLeZGajzUbhbp69k8/UD03dT8NBDMSos5XayJNnEibM2unImh6tcOek5prenHQOqkIv7TeGfC3HQDxUgXH2Rw8j+7Kyu/p72AYTCvXrJOoAVJ00KKDXTi4xu7+a5VJwP/tpdLz5jeoIfivzgxPP9I/o72OhSrdAZcxPQ5YjbyS22IXhz7G1MkHX0ItytWRqKyfXjq+58LS2ovlQu3eYhoftfBjsq3xisdjqTld9V+DL97qCcWzHo7hscMLO7/5nrXsGiSY16PZ6tUtqe9lI4ErvC+71iH+i44NijMTXMt9uX01V/4Wqlz8m5sDE4Nl0uM31eV2M1MvLKyV1tntj78WREX/mpuqclD8wWO+weglzqfyaF/"

# your secret key
secretKey = "cd07b3c95dc9a0c8e9318b29bdc13b03"

print("encryptedIpnResponse: " + encryptedIpnResponse)
print("secretKey: " + secretKey)

# get the IPN response
jsonResponse = Twispay.decrypt_ipn_response(encryptedIpnResponse, secretKey)

print("Decrypted IPN response: " + str(jsonResponse))
