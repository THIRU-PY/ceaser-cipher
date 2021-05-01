def decrypt(enc_msg,en_shift): # function to dencrypt the message
  de_msg=""
  de_shift=int(input("\nWhat is the shift:\t"))
  if de_shift==en_shift:
    for char in enc_msg:
      if char!=" ":
        conv_char=ord(char)
        de_char=chr(conv_char-de_shift)
        de_msg+=de_char
      else:
        de_msg+=char
  else:
    print("\nWrong decode shift")
  return de_msg