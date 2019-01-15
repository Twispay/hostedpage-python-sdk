import hmac
import hashlib
import base64
import json
from Crypto.Cipher import AES

class Twispay:
    """
    The Twispay class implements methods to get the value
    of `jsonRequest` and `checksum` that need to be sent by POST
    when making a Twispay order and to decrypt the Twispay IPN response.
    """
    def __init__(self):
        pass

    @staticmethod
    def get_base64_json_request(dict_order_data):
        """Get the `jsonRequest` parameter (order parameters as JSON and base64 encoded).

        :param dict_order_data: The order parameters.
        :type dict_order_data: dict

        :return str
        """
        return base64.b64encode(json.dumps(dict_order_data).encode("ascii")).decode("utf8")

    @staticmethod
    def get_base64_checksum(dict_order_data, secret_key):
        """Get the `checksum` parameter (the checksum computed over the `jsonRequest` and base64 encoded).

        :param dict_order_data: The order parameters.
        :type dict_order_data: dict
        :param secret_key: The secret key (from Twispay).
        :type secret_key: str

        :return str
        """
        hmac_sha512 = hmac.new(secret_key.encode("ascii"), json.dumps(dict_order_data).encode("ascii"), hashlib.sha512).digest()
        return base64.b64encode(hmac_sha512).decode("utf-8")

    @staticmethod
    def decrypt_ipn_response(encrypted_ipn_response, secret_key):
        """Decrypt the IPN response from Twispay.

        :param encrypted_ipn_response
        :type encrypted_ipn_response: str
        :param secret_key: The secret key (from Twispay).
        :type secret_key: str

        :return str
        """
        # get the IV and the encrypted data
        encrypted_parts = encrypted_ipn_response.split(',', 2)
        iv = base64.b64decode(encrypted_parts[0])
        encrypted_data = base64.b64decode(encrypted_parts[1])

        # decrypt the encrypted data
        cipher = AES.new(secret_key, AES.MODE_CBC, iv)
        decrypted_ipn_response = cipher.decrypt(encrypted_data).decode('utf-8')

        # JSON decode the decrypted data
        return json.loads(decrypted_ipn_response)
