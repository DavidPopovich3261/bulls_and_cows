import random

def generate_secret(length: int = 4,unique_digits: bool = True) -> str:
    secret=''
    while len(secret)<length:
        rng=str(random.randint(0,9))
        if unique_digits:
            if not rng in secret:
                secret+=rng
        else:
            secret += rng
    return secret





