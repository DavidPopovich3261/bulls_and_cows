

def is_valid_guess(guess: str, length: int, unique_digits: bool = True)->bool:
    flag=True
    if len(guess)==length:
        if not guess.isdigit():
            flag=False
            print()
        elif unique_digits:
            guess2=''
            for i in guess:
                if i in guess2:
                    flag =False
                    print()
                else:
                    guess2+=i
        return flag



def is_new_guess(guess: str, seen) -> bool:
    if guess in seen:
        return False
    return True