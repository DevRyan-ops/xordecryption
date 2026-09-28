# XOR Decryption Tool

A lightweight Python utility for decrypting Base64-encoded data encrypted with XOR ciphers. This tool supports flexible key input (single-byte, color codes, or custom hex keys) and outputs results in multiple formats (hex, UTF-8, Latin-1).

## Features

- **Base64 Decoding**: Automatically decodes Base64-encoded encrypted data
- **XOR Decryption**: Decrypts using a repeating cyclic key
- **Flexible Key Input**: 
  - Single-byte hex keys (e.g., `FF`)
  - Color codes (e.g., `#FFFFFF` → RGB bytes)
  - Custom hex byte sequences (e.g., `FF 0A 3C`)
- **Multiple Output Formats**: Hex, UTF-8, and fallback Latin-1 decoding
- **Type Hints**: Fully typed for better code reliability
- **Interactive CLI**: User-friendly command-line interface

## Installation

Clone the repository:

```bash
git clone https://github.com/DevRyan-ops/xordecryption.git
cd xordecryption
```

No external dependencies required—uses only Python's standard library.

## Usage

### Interactive Mode

Run the script to use the interactive prompt:

```bash
python xordecryption.py
```

Then follow the prompts:

1. **Enter Base64 string**: Paste your Base64-encoded encrypted data
2. **Choose key mode**:
   - `1` = Single-byte key (e.g., `FF`)
   - `2` = Color code key (e.g., `#FFFFFF`)
   - `3` = Custom hex bytes (e.g., `FF 0A 3C`)
3. **View results** in hex and text formats

### Programmatic Usage

```python
from xordecryption import xor_base64_decode

# Decrypt with color code key
js_b64 = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D"
key = "#0000BB"

# Get bytes output
plaintext_bytes = xor_base64_decode(js_b64, key)
print(plaintext_bytes.hex())

# Get decoded string output
plaintext_text = xor_base64_decode(js_b64, key, output_encoding='utf-8')
print(plaintext_text)
```

## Function Reference

### `xor_base64_decode(b64_input, key, *, output_encoding=None)`

Decodes Base64 and XOR-decrypts the result.

**Parameters:**
- `b64_input` (str): Base64-encoded encrypted data
- `key` (str or bytes): XOR key (will cycle if shorter than data)
- `output_encoding` (str, optional): Character encoding for output (e.g., `'utf-8'`). If `None`, returns raw bytes

**Returns:**
- `bytes` or `str`: Decrypted data in requested format

**Raises:**
- `ValueError`: If key is empty

**Example:**

```python
result = xor_base64_decode("HmYkBw...", "#0000BB", output_encoding='utf-8')
```

### `xor_decrypt(data, key)`

Core XOR decryption function (commented in original code).

```python
def xor_decrypt(data: bytes, key: bytes) -> bytes:
    """XOR decrypt using a repeating key."""
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
```

## How It Works

### XOR Cipher Basics

The XOR (exclusive OR) operation is reversible:

```
plaintext ⊕ key = ciphertext
ciphertext ⊕ key = plaintext
```

### Process Flow

1. **Base64 Decode**: Convert Base64 string → raw encrypted bytes
2. **Cycle Key**: Repeat key across data length if needed
3. **XOR Each Byte**: `output[i] = encrypted[i] ⊕ key[i % key_length]`
4. **Decode Output**: Interpret bytes as text (UTF-8, Latin-1, or hex)

### Example

```
Encrypted (hex):  1E 66 24 07
Key (hex):        BB BB BB BB
XOR Result:       A5 DC 99 BC
Decoded:          "..."
```

## Examples

### Example 1: Single-Byte Key

```python
result = xor_base64_decode("SGVsbG8gV29ybGQ=", "FF", output_encoding='utf-8')
```

### Example 2: Color Code Key

```python
# Decrypts JavaScript obfuscated with #0000BB (blue) key
result = xor_base64_decode("HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D", "#0000BB", output_encoding='utf-8')
```

### Example 3: Custom Hex Key

```python
result = xor_base64_decode("AAAA", "FF 0A 3C", output_encoding='latin-1')
```

## Use Cases

- **Reverse Engineering**: Decode obfuscated JavaScript or payloads
- **CTF/Puzzle Solving**: Decrypt XOR-based challenges
- **Malware Analysis**: Unpack simple XOR-encrypted strings
- **Educational**: Learn XOR cipher mechanics
- **Data Recovery**: Attempt to decrypt known-key encrypted data

## Security Note

⚠️ **XOR encryption is NOT cryptographically secure.** It provides only obfuscation, not true encryption. Use this tool for:
- Educational purposes
- Reverse engineering challenges
- Legacy system decryption

**Never use XOR for:**
- Protecting sensitive data
- Production encryption
- Compliance-required security

For production security, use modern algorithms like AES-256, ChaCha20, or cryptographic libraries like `cryptography` or `PyCryptodome`.

## Contributing

Contributions welcome! Ideas:
- Add file I/O support for large encrypted files
- Implement frequency analysis for key recovery
- Add more output format options
- Support additional cipher modes

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or issues, open an issue on [GitHub](https://github.com/DevRyan-ops/xordecryption).
