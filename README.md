# x16rt_hash

A Python C extension module for the X16RT proof-of-work hash function. This module provides high-performance cryptographic hashing used in blockchain mining.

## Features

- **Fast C implementation** - Compiled C extension for optimal performance
- **Python 3.8+** - Modern Python support (Python 2 no longer supported)
- **Deterministic** - Same input always produces the same output
- **32-byte output** - Produces 256-bit hash digests
- **Cross-platform** - Works on Linux, macOS, and Windows

## Prerequisites

### Linux (Ubuntu/Debian)

```bash
sudo apt-get install python3-dev build-essential
```

### macOS

```bash
xcode-select --install
```

### Windows

- Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) or Visual Studio Community
- Or use MinGW-w64

## Installation

### From Source

Clone the repository and install:

```bash
git clone https://github.com/AvianNetwork/x16rt_hash.git
cd x16rt_hash
pip install -e .
```

### For Development

Install in editable mode with development tools:

```bash
pip install -e ".[dev]"
```

## Usage

```python
import x16rt_hash
from binascii import hexlify, unhexlify

# Input must be exactly 80 bytes (typical blockchain block header)
input_data = unhexlify('0000002049963e9e46701e28e2dd44f61dea241ba3a457979fa3b378822c6cc24457bc2500a0da644814e2a43cc163f3f37590982e1e2f5ac45d1de2f8222750fea1c844f8d2315c824d111b120979e30000')

# Generate hash
hash_result = x16rt_hash.getPoWHash(input_data)

# Display as hex string
print(hexlify(hash_result).decode())
# Output: 40abc3e30ba0552a7910c0acd5b46a5f8dbf287e0108ee679d59070000000000
```

## API Reference

### `getPoWHash(data: bytes) -> bytes`

Computes the X16RT proof-of-work hash.

**Parameters:**

- `data` (bytes): Input data, must be exactly 80 bytes

**Returns:**

- `bytes`: 32-byte hash digest

**Raises:**

- `TypeError`: If input is not bytes
- `ValueError`: If input length is not exactly 80 bytes

## Testing

Run the comprehensive test suite:

```bash
# Run the test script
python test.py

# Or using unittest discovery
python -m unittest discover

# Or using pytest (if installed)
pytest test.py -v
```

The test suite includes:

- Known hash vector validation
- Output format and size verification
- Determinism checking
- Invalid input handling

## Building Wheels

Build distribution wheels for all supported platforms:

```bash
pip install cibuildwheel
cibuildwheel --output-dir wheelhouse
```

This requires Docker on Linux or can use native build tools on macOS/Windows.

## Supported Python Versions

- Python 3.8+
- CPython only (PyPy not supported due to C extension)

## Algorithm Details

X16RT combines 16 cryptographic hash algorithms in a sequence determined by the block timestamp:

- **Base algorithms**: BLAKE, BMW, CubeHash, Echo, Fugue, Grøstl, HAMSI, JH, Keccak, Luffa, SHABAL, SHAvite, SIMD, Skein, Whirlpool, SHA-512
- **Time-based ordering**: The algorithm sequence is determined by hashing the block timestamp
- **Sequential hashing**: Each algorithm's output becomes the input to the next
- **Output**: Final 32 bytes of the result hash

For more details on the algorithm, see the comments in `x16rt.c`.

## Contributing

Contributions are welcome! Please ensure:

- Code follows existing style conventions
- Changes include tests
- All tests pass: `python test.py`

## License

Licensed under the MIT/X11 software license. See the [LICENSE](LICENSE) file for details.

## Authors

- Original X16R algorithm: The Ravencoin Core developers
- X16RT implementation: The Veil Core developers
- Current maintainers: The Avian Core developers
