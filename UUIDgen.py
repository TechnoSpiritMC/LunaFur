import random
import uuid
import hashlib
import time

"""
This is a small lib file with the purpose of
generating game IDs. It can generate UUIDs with
a custom pattern and generation method or create
LunaFur's own game IDs that consist of just
a hexadecimal number (which was the time when
the game was created) and a random number at
the end to guarantee randomness and so that the
generayed ID is unique.
"""

def generate_uuid(seed):
    hash_object = hashlib.md5(seed.encode())
    player_hash = hash_object.hexdigest()
    random_uuid = uuid.uuid4()
    custom_uuid = uuid.UUID(int=(random_uuid.int & 0xFFFFFFFFFFFF0000) | int(player_hash[:12], 16))
    return custom_uuid


def generateID():
    u0 = str(hex(random.randint(0, 4294967295)))
    u1 = str(hex(random.randint(0, 65535)))
    u2 = str(hex(random.randint(0, 65535)))
    u3 = str(hex(random.randint(0, 281474976710655)))

    return u0[2:] + "-" + u1[2:] + "-" + u2[2:] + "-" + u3[2:]
    
def generateameID():
    _1 = str(time.time())
    _2 = str(random.randint(0, 10000))
    return(hex(int(_1+_2)))

# ======================================================================================================================
#                             This file is a part of TechnoSpirit's LunaFur bot. If you want
#                             to modify it, or do your own version, but you are taking parts
#                             of this version, please leave this text at the end of the file
#                                                           ---
#                             Thank you for using LunaFur and I hope it satisfied your needs
#
# ======================================================================================================================
