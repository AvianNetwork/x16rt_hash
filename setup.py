from setuptools import setup, Extension
from pathlib import Path

# Read long description from README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

x16rt_hash_module = Extension(
    "x16rt_hash",
    sources=[
        "x16rt_module.c",
        "x16rt.c",
        "sha3/blake.c",
        "sha3/bmw.c",
        "sha3/groestl.c",
        "sha3/jh.c",
        "sha3/keccak.c",
        "sha3/skein.c",
        "sha3/cubehash.c",
        "sha3/echo.c",
        "sha3/luffa.c",
        "sha3/sha2.c",
        "sha3/simd.c",
        "sha3/hamsi.c",
        "sha3/hamsi_helper.c",
        "sha3/fugue.c",
        "sha3/shavite.c",
        "sha3/shabal.c",
        "sha3/whirlpool.c",
        "sha3/sha2big.c",
    ],
    include_dirs=[".", "./sha3"],
)

setup(
    name="x16rt_hash",
    version="0.2.0",
    description="Python 3 bindings for X16RT hashing PoW",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Brian Lee, random.zebra",
    maintainer="The Avian Core Developers",
    url="https://github.com/AvianNetwork/x16rt_hash",
    project_urls={
        "Bug Tracker": "https://github.com/AvianNetwork/x16rt_hash/issues",
        "Source Code": "https://github.com/AvianNetwork/x16rt_hash",
    },
    python_requires=">=3.8",
    ext_modules=[x16rt_hash_module],
)
