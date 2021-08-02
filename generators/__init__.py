import hashlib
import random



def generate_random_hash():
    """
        A function to generate a random hash string.
        The string contains 32 characters. The function
        uses hashlib.md5 with parameters as random.random
        combined with random.randint to produce almost 
        un repeatable hash strings.
    """

    starter = int(1000*random.random())

    _from = random.randint(
        starter*100,
        random.randint(
            starter,
            int(
                starter * 1000000 ** int( random.random()*10 )
            )
        )
    )
    _till = _from * random.randint(0, _from)
    result = hashlib.md5(
        str(
            random.randint(_from, _till)**2
        ).encode('utf-8')
    )
    return result.hexdigest()



def generate_random_password(c=0, l=16):
    """
        Generates a random password.
        There are 
    """
    symbols = "~!@#$%^&*()_+=-`{}[]:;'\",.<>/?|\\"
    numbers = "1234567890"
    small_chars = "qwertyuiopasdfghjklzxcvbnm"
    capit_chars = "QWERTYUIOPASDFGHJKLZXCVBNM"

