import random

# Generating three four groups of two random number/letter combinations
mac = [ 0x00, 0x24, 0x81,
    random.randint(0x00, 0x7f),
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff) ]

complete_mac= ''.join(map(lambda x: "%02x" % x, mac))

print complete_mac.upper()
