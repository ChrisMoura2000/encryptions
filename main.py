'''
 WARNING 
  - Validar se não tem números no texto para criptografar nas duas funções
  - Criar um while para manter o programa executando e só sair caso o usuario queira
'''
from cesars_cipher import cesar_cipher
from vigenere_cipher import vigenere_cipher
from frequency_analysis import frequency_analysis

def encryption():    
  print("----------------------------------")
  print("Digite um número para selecionar o tipo de criptografia:")
  print("[1] Cifra de Cesar")
  print("[2] Cifra de Vigènere")
  encrypt_type = input("")

  while encrypt_type != "1" and encrypt_type != "2":
    print("----------------------------------")
    print("Valor invalido. Digite um número para selecionar o tipo de criptografia: ")
    print("[1] Cifra de Cesar")
    print("[2] Cifra de Vigenere")
    encrypt_type = input("")
  
  print("----------------------------------")
  is_decrypting = input("Digite [0] para criptografar ou [1] para descriptografar: ")
  while is_decrypting != "0" and is_decrypting != "1":
    is_decrypting = int(input("Valor invalido. Digite [0] para criptografar ou [1] para descriptografar: "))

  
  if encrypt_type == "1":
    # print("Você escolheu Cifra de Cesar por padrão serão três letras deslocadas para direita masss")
    # print("Aqui você tem opção de personalizar esse valor =D")
    # steps = input("Digite um número entre 1 e 25 para definir a quantidade de casas a serem deslocadas: ")
    # while not steps.isdigit():
    #   steps = input("Valor inválido digite apenas numeros (de 1 até 25): ")
    # while int(steps) < 1 or int(steps) > 25:
    #   steps = input("Valor inválido digite apenas numeros (de 1 até 25): ")
    
    text = input("Dgite o texto para ver o resultado: ")
    text_encripted = cesar_cipher(text, is_decrypting=int(is_decrypting))
    print(text_encripted)
  elif encrypt_type == "2":
    keyword = input("Digite a palavra-chave que deseja usar para criptografar sua mensagem: ")
    while not keyword.isalpha():
      keyword = input("A palavra-chave deve ser apenas letras. Digite novamente: ")

    text = input("Dgite o texto para ver o resultado: ")
    text_encripted = vigenere_cipher(text, keyword, is_decrypting=int(is_decrypting))
    print(text_encripted)  

# encryption()

my_text = "No meio do caminho tinha uma pedra Tinha uma pedra no meio do caminho Tinha uma pedra No meio do caminho tinha uma pedra Nunca me esquecerei desse acontecimento Na vida de minhas retinas tao fatigadas"

ciphred_message = cesar_cipher(my_text, 3)

print(frequency_analysis(ciphred_message))
print(frequency_analysis(my_text))