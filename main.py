
import re
from TelefonesBR import TelefonesBr

# from cpf_cnpj import Documento
# exemplo_cnpj = "06256423000153"

# documento = Documento.cria_documento(exemplo_cnpj)
# print(documento)



## teste regex 01
# padrao = "[0-9][a-z]{2}[0-9]"
# texto = "123 1ac2 1cc aa1"

# resposta = re.search(padrao, texto)
# print(resposta.group())

## teste regex email
# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# texto = "alkdjshfa adsfljk rlaecio@hotmail.com lh ;lkjdsf"

# resposta = re.search(padrao, texto)
# print(resposta.group())

telefone = "3512126481234"
telefone_objeto = TelefonesBr(telefone)
# padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})" 

# resposta = re.findall(padrao, telefone)
# resposta = re.search(padrao, telefone)
# print(resposta.group(2))
print(telefone_objeto)