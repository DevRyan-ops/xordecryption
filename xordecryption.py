# import base64

# def xor_decrypt(data: bytes, key: bytes) -> bytes:
#     """XOR decrypt using a repeating key."""
#     return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

# def main():
#     print("\n=== XOR DECRYPT TOOL ===\n")

#     # Get Base64 data
#     b64_input = input("Enter Base64 string to decrypt: ").strip()

#     # Decode Base64 safely
#     try:
#         encrypted_data = base64.b64decode(b64_input)
#     except Exception as e:
#         print("Error decoding Base64:", e)
#         return

#     print(f"\nDecoded {len(encrypted_data)} bytes of encrypted data.")

#     print("\nChoose XOR key mode:")
#     print("  1 = Single-byte key (e.g., FF)")
#     print("  2 = 3-byte key from color code (e.g., #FFFFFF → FF FF FF)")
#     print("  3 = Custom key (hex bytes)")

#     mode = input("\nSelect option (1/2/3): ").strip()

#     # Handle key input
#     if mode == "1":
#         key_hex = input("Enter single hex byte key (e.g., FF): ").strip()
#         key = bytes([int(key_hex, 16)])

#     elif mode == "2":
#         color = input("Enter color code (e.g., #FFFFFF): ").strip()
#         color = color.replace("#", "")
#         if len(color) != 6:
#             print("Invalid color code")
#             return
#         key = bytes.fromhex(color)

#     elif mode == "3":
#         custom = input("Enter hex bytes (e.g., FF 0A 3C): ").replace(" ", "")
#         try:
#             key = bytes.fromhex(custom)
#         except:
#             print("Invalid hex format")
#             return
#     else:
#         print("Invalid option.")
#         return

#     # Decrypt
#     decrypted = xor_decrypt(encrypted_data, key)

#     print("\n=== DECRYPTION RESULT ===")
#     print("\nHex output:")
#     print(decrypted.hex())

#     print("\nText output:")
#     try:
#         print(decrypted.decode("utf-8"))
#     except:
#         print(decrypted.decode("latin-1", errors="replace"))

#     print("\n=== DONE ===\n")


# if __name__ == "__main__":
#     main()

import base64
from typing import Union

def xor_base64_decode(b64_input: str, key: Union[str, bytes], *,
                       output_encoding: Union[str, None] = None) -> Union[bytes, str]:
    """
    Decode a Base64-encoded byte stream, XOR it with `key` (cycled), and return bytes
    or a decoded string if output_encoding is provided.
    """
    # Decode Base64 -> raw encrypted bytes
    enc_bytes = base64.b64decode(b64_input)

    # Ensure key is bytes
    key_bytes = key if isinstance(key, bytes) else key.encode('utf-8')
    if len(key_bytes) == 0:
        raise ValueError("key must not be empty")

    # XOR each byte with corresponding key byte (cycled)
    out = bytearray(len(enc_bytes))
    klen = len(key_bytes)
    for i, b in enumerate(enc_bytes):
        out[i] = b ^ key_bytes[i % klen]

    result = bytes(out)
    return result.decode(output_encoding) if output_encoding else result

# Example usage:
js_b64 = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D"
key = "#0000BB"
plaintext_bytes = xor_base64_decode(js_b64, key)
plaintext_text = xor_base64_decode(js_b64, key, output_encoding='utf-8')
