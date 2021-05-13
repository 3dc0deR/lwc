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

# Output

**1. Present**

Present on android:
![Present Android](/output/present_android.png)


Present on raspberry pi:
![Present raspberry pi](/output/present_rpi.png)


Present on windows:
![Present windows](/output/present_win.png)

**2. Trivium**

Trivium on android:
![Trivium Android](/output/trivium_android.png)


Trivium on raspberry pi:
![Trivium raspberry pi](/output/trivium_rpi.png)


Trivium on windows:
![Trivium windows](/output/trivium_win.png)

**3. ELLI**

ELLI on android:
![ELLI Android](/output/elli_android.png)


ELLI on raspberry pi:
![ELLI raspberry pi](/output/elli_rpi.png)


ELLI on windows:
![ELLI windows](/output/elli_win.png)

**4. SPONGENT**

SPONGENT on android:
![SPONGENT Android](/output/spongent_android.png)


SPONGENT on raspberry pi:
![SPONGENT raspberry pi](/output/spongent_rpi.png)


SPONGENT on windows:
![SPONGENT windows](/output/spongent_win.png)

**5. Chaskey**

Chaskey on android:
![Chaskey Android](/output/chaskey_android.png)


Chaskey on raspberry pi:
![Chaskey raspberry pi](/output/chaskey_rpi.png)


Chaskey on windows:
![Chaskey windows](/output/chaskey_win.png)
