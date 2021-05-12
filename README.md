# Light Weight Cryptography

Implementation of various light weight cryptography algorithms in python.

Code has been taken from following sources:

1. Present - Symmetric light-weight block cipher: https://asecuritysite.com/encryption/present
2. Trivium - Light-weight stream cipher: https://asecuritysite.com/encryption/trivium
3. ELLI - Light-weight asymmetric cipher: https://asecuritysite.com/encryption/elli
4. SPONGENT - Light-weight hash function: https://asecuritysite.com/encryption/spongent2
5. Chaskey - Light-weight MAC function: https://asecuritysite.com/encryption/chas2


All code is based on python3 except for ELLI which is only working on python2 due to some dependency issues.

# Dependencies

Present:

Padding - Can be installed with "pip3 install padding".

ELLI:

eccsnacks - The version 1.0.2 fails to install in both python2 and python3. However, version 1.0.1 works fine and the code runs successfully on python2. It can be installed with "pip install eccsnacks==1.0.1".
