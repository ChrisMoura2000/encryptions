def vigenere_cipher(phrase, keyword, is_decrypting=False):
  phrase = phrase.lower()
  original_alphabet = [chr(x) for x in range(97, 122 + 1)]
  matriz_vigenere = [[] for x in range(26)]
  cipher_phrase = ""
  for x in range(26):
    matriz_vigenere[x] = [*original_alphabet[x:], *original_alphabet[:x]]
  
  matriz_to_encrypt = []
  for letter_key in keyword:
    for line in matriz_vigenere:
      if line[0] == letter_key:
        matriz_to_encrypt.append(line)

  if is_decrypting:
    index_key = 0
    for i in range(len(phrase)):
      if index_key == len(keyword):
        index_key = 0
      if phrase[i] == " ":
        cipher_phrase += " "
        index_key += 1
      elif phrase[i] not in original_alphabet:
        cipher_phrase += phrase[i]
        index_key += 1
      else:
        cipher_phrase += original_alphabet[matriz_to_encrypt[index_key].index(phrase[i])]
        index_key += 1
    
    return cipher_phrase


  index_key = 0
  for i in range(len(phrase)):
    if index_key == len(keyword):
      index_key = 0
    if phrase[i] == " ":
      cipher_phrase += " "
      index_key += 1
    elif phrase[i] not in original_alphabet:
      cipher_phrase += phrase[i]
      index_key += 1
    else:
      cipher_phrase += matriz_to_encrypt[index_key][original_alphabet.index(phrase[i])]
      index_key += 1
  
  return cipher_phrase
  
if __name__ == "__main__":
  my_phrase = vigenere_cipher("hellooo 7 world", "white")
  print(my_phrase)
  my_phrase = vigenere_cipher("dlteskv 2 psnsl", "white", is_decrypting=True)
  print(my_phrase)


