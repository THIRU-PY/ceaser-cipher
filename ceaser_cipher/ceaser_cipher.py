from encryption import encrypt
from decryption import decrypt
print('''
█▀▀ █▀▀▄ █▀▀ █▀▀█ █──█ █▀▀█ ▀▀█▀▀ 　 █▀▀█ █▀▀▄ █▀▀▄ 　 █▀▀▄ █▀▀ █▀▀ █▀▀█ █──█ █▀▀█ ▀▀█▀▀ 
█▀▀ █──█ █── █▄▄▀ █▄▄█ █──█ ──█── 　 █▄▄█ █──█ █──█ 　 █──█ █▀▀ █── █▄▄▀ █▄▄█ █──█ ──█── 
▀▀▀ ▀──▀ ▀▀▀ ▀─▀▀ ▄▄▄█ █▀▀▀ ──▀── 　 ▀──▀ ▀──▀ ▀▀▀─ 　 ▀▀▀─ ▀▀▀ ▀▀▀ ▀─▀▀ ▄▄▄█ █▀▀▀ ──▀──''')


message=input("\nEnter your message:\t")
en_shift=int(input("\nHow many Shifts:\t"))
en_msg=encrypt(message,en_shift)
print(f"\nEncrypted message:\t{en_msg}")
choice=input("\nYou want to decrypt the message (y/n)\t").lower()
if choice=='y':
  print(f"\nDecrypted message:\t{decrypt(en_msg,en_shift)}")