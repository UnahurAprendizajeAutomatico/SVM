import cv2

def sxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
def byte_xor(ba1, ba2):
    return bytes([int(_a) ^ int(_b) for _a, _b in zip(ba1, ba2)])


art_file = open("backup_files/art.txt", "r+b")
art_file_enc = open("encrypted/art.txt.enc", "r+b")


bitstream = byte_xor(art_file.read(), art_file_enc.read())

flag_file = open("encrypted/ideas.txt.enc", "r+b")

decrypted = byte_xor(bitstream, flag_file.read())
print(decrypted)
