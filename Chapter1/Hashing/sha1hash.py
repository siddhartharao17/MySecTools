import hashlib
salt = 'HX'
data = 'hey'
sha512 = hashlib.sha512()
sha512.update(salt+data)
print sha512.hexdigest().upper()

