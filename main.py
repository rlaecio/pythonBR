import re

from TelefonesBR import TelefonesBr
from Busca_Endereco import BuscaEndereco



# from cpf_cnpj import Documento
# exemplo_cnpj = "06256423000153"

# documento = Documento.cria_documento(exemplo_cnpj)
# print(documento)
# from datetime import datetime, timedelta
# from Datas_BR import DatasBr

# cadastro = DatasBr()
# print(cadastro)

# print(cadastro.momento_cadastro)
# print(cadastro.mes_cadastro())
# print(cadastro.dia_semana())

# hoje = datetime.today()
# data_formatada = hoje.strftime("%d/%m/%Y")
# print(data_formatada)


# hoje = DatasBr()
# print(hoje.tempo_cadastro())


cep = "01001000"
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)