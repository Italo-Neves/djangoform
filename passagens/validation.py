
def origem_destino_iguais(origem,destino,lista_erros):
    """verifica se os destinos são iguais"""
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais!'

def campo_tem_numero(valor_campo, nome_campo, lista_erros):
    """Verifica se possui algum digito númeorico"""
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Não inclua números neste campo'

def data_ida_maio_volta(data_ida,data_volta,lista_erros):
    """Verifica se a data de ida é maior que a data de volta"""
    if data_ida > data_volta:
        lista_erros['data_ida'] = 'Data de volta não pode ser menor que a data de ida' 

def data_ida_hoje(data_ida, data_pesquisa, lista_erros):
    """Verifica se a data de ida é menor que a data de hoje"""
    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = 'Data de ida não pode ser menor que a data de hoje!'
    