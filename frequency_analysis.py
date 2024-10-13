def print_graphic(frequency_letters, alphabet):
  heigh_frequency = max(frequency_letters)
  for i in range(heigh_frequency, 0, -1):
    line = ""
    for value in frequency_letters:
      if value >= i:
        line += "|"
      else:
        line += " "
      line += " "
    print(line)
  print(" ".join(alphabet))
  

def frequency_analysis(text_to_analysis):
  original_alphabet = [chr(x) for x in range(97, 122 + 1)]
  frequency_letters = [0 for x in range(26)]
  text_without_spaces = text_to_analysis.lower()
  cc = 0
  for text_letter in text_without_spaces:
    if text_letter in original_alphabet:
      frequency_letters[original_alphabet.index(text_letter)] += 1
    cc += 1
  return original_alphabet, frequency_letters

if __name__ == "__main__":

  my_text = "No meio do caminho tinha uma pedra Tinha uma pedra no meio do caminho Tinha uma pedra No meio do caminho tinha uma pedra. Nunca me esquecerei desse acontecimento Na vida de minhas retinas tão fatigadas. Nunca me esquecerei que no meio do caminho Tinha uma pedra Tinha uma pedra no meio do caminho No meio do caminho tinha uma pedra"
  alphabet, frequency = frequency_analysis(my_text)
  print_graphic(frequency, alphabet)