s = "Привет!"

utf8 = s.encode()
print(utf8) # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'

utf16 = s.encode('utf-16')
print(utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'

s_from_utf16 = utf16.decode('utf-16')
print(s_from_utf16 == s)  # True