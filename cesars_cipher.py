def cesar_cipher(phrase="", steps=3, is_decrypting=False):
  phrase = phrase.lower()
  original_alphabet = [chr(x) for x in range(97, 122 + 1)]
  cipher_alphabet = [*original_alphabet[steps:], *original_alphabet[:steps]]
  cipher_phrase = ""

  if is_decrypting:
    for letter in phrase:
      if letter == " ":
        cipher_phrase += " "
      else:
        cipher_phrase += original_alphabet[cipher_alphabet.index(letter)]
    return cipher_phrase
  
  for letter in phrase:
    if letter == " ":
      cipher_phrase += " "
    else:
      cipher_phrase += cipher_alphabet[original_alphabet.index(letter)]
  return cipher_phrase

if __name__ == "__main__":
  text = "teste de texto nao cifrado"
  my_phrase = cesar_cipher(text)
  print(my_phrase)
  my_phrase = cesar_cipher("khoor zruog", is_decrypting=True)
  print(my_phrase)