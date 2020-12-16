import hashlib


def generateHash(password):
    hashed_pass = hashlib.md5(password.encode()).hexdigest()
    return hashed_pass