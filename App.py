import hashlib, os, string
##Hash the link using sha256
def hash_link(link):
    salt=os.urandom(16).hex()
    sha256=hashlib.sha256()
    sha256.update((link+salt).encode('utf-8'))
    FHash=conv_base62(int(sha256.hexdigest(),16))
    return FHash[:7],FHash,link,salt

##convert hash to Base 62 AS HBase
def conv_base62(num):
    symbols=string.digits+string.ascii_lowercase+string.ascii_uppercase
    if num == 0:
        return symbols[0]
    HBase=[]
    while num>0:
        HBase.insert(0, symbols[num % 62])
        num= num // 62
    return ''.join(HBase)







