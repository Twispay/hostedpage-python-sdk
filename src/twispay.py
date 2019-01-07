import hmac
import hashlib
import base64
import json
from Crypto.Cipher import AES


class Twispay:
    def __init__(self):
        pass

    @staticmethod
    def get_base64_json_request(dict_order_data):
        return base64.b64encode(json.dumps(dict_order_data).encode("ascii")).decode("utf8")

    @staticmethod
    def get_base64_checksum(dict_order_data, secret_key):
        hmac_sha512 = hmac.new(secret_key.encode("ascii"), json.dumps(dict_order_data).encode("ascii"), hashlib.sha512).digest()
        return base64.b64encode(hmac_sha512).decode("utf-8")

    @staticmethod
    def get_html_order_form(dict_order_data, secret_key, twispay_live=False):
        base64_json_request = Twispay.get_base64_json_request(dict_order_data)
        base64_checksum = Twispay.get_base64_checksum(dict_order_data, secret_key)
        host_name = ("secure-stage.twispay.com", "secure.twispay.com")[twispay_live]
        return """<form action="https://""" + host_name + """" method="post" accept-charset="UTF-8">
    <input type="hidden" name="jsonRequest" value=\"""" + base64_json_request + """\">
    <input type="hidden" name="checksum" value=\"""" + base64_checksum + """\">
    <input type="submit" value="Pay">
</form>
"""

    @staticmethod
    def decrypt_ipn_response(encrypted_ipn_response, secret_key):
        # get the IV and the encrypted data
        encrypted_parts = encrypted_ipn_response.split(',', 2)
        iv = base64.b64decode(encrypted_parts[0])
        encrypted_data = base64.b64decode(encrypted_parts[1])

        # decrypt the encrypted data
        cipher = AES.new(secret_key, AES.MODE_CBC, iv)
        decrypted_ipn_response = cipher.decrypt(encrypted_data).decode('utf-8')

        # JSON decode the decrypted data
        return json.loads(decrypted_ipn_response)
