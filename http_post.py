import requests

# definição da url e parâmetros usando type hints
url: str = "https://tranquil-rex-405218.rj.r.appspot.com/hashCodeServer"
paramametros_da_requisicao: dict = { 'nome': 'David Silveira', 'email': 'meuemail@email.com', 
                              'cpf': '222.222.222-22'} # cpf alegórico    
# função para envio do POST 
def envia_requisicao() -> requests:
    return requests.post(url, params=paramametros_da_requisicao)

# Parâmetro de resposta da requisição
# Função que retorna uma String formatada da resposta da requisição
resposta_json: dict = envia_requisicao().json()
def apresenta_retorno_request() -> str:
    return f'\nCódigo hash: {resposta_json["hashCode"]}\nStatus code: {resposta_json["status"]}\nPergunta: {resposta_json["pergunta"]}\n'
    
# chamada da função principal 
if __name__ == "__main__":
    print(apresenta_retorno_request())
     