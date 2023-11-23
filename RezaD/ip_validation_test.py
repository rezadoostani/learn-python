from IPvalidation import *

assert check('-1.-2.-3.-4') == "Invalid Ip address"
assert check('256.349.300.400') == "Invalid Ip address"
assert check('1.2.4.5') == "Valid Ip address"
