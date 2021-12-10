from random import SystemRandom
from hmac import compare_digest

_sysrand = SystemRandom()

randbits = _sysrand.getrandbits
choice = _sysrand.choice


api_key = 'O9OMm8sclDurbeI9s7d4q0eDRL8XRx5O'