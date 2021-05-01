def encrypt(message,en_shift): # function to encrypt the message
  en_msg=""
  for char in message:
    if char!=" ": # neglect space
      conv_char=ord(char) # ord()- gives a integetr representing charecter provided 
      en_char=chr(conv_char+en_shift)
      en_msg+=en_char
    else:
      en_msg+=char

  return en_msg