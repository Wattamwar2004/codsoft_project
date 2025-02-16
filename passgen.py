import secrets
import string

def generate_password(lenght=12):
    if lenght < 4:
        raise ValueError("password lenght must be at least 4 characters.")
        i
        letters = string.ascii_letters
        digits = string.digits
        special_characters = string.punctuation
        password = [
            secrets.choice(letters),
            secrets.choice(digits),
            secrets.choice(special_characters),
            secrets.choice(letters + digits + special_characters)
        ]
        all_characters = letters + digits + special_characters
        password += [secrets.choice(all_characters)] 
        for _ in range(length - 4):
         secrets.SystemRandom().shuffle(password)
        return ''.join(password)
    print("gentare password:", generate_password(12))