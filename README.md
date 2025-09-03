# Meu sistema
Um sistema simples em python que busca fotos de cachorrinhos

## Instalação
```bash
git clone https://github.com/JoaoPauloBernardo/Aula_C14
cd repositorio
npm install
```

## Regressão documentada

Durante a atividade, um colega fez um Pull Request alterando a função `get_cat_image` para retornar `data["url"]` em vez de `data["message"]`.

### Erro encontrado
Ao rodar o sistema e os testes após essa mudança, ocorreu o seguinte erro:
Traceback (most recent call last):
File "c:\Users\joaop\meu_sistema\main.py", line 17, in main
print("URL da imagem:", get_cat_image())
File "c:\Users\joaop\meu_sistema\main.py", line 9, in get_cat_image
data = response.json()
File "C:\Python310\lib\site-packages\requests\models.py", line 978, in json
raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)


Esse erro ocorre porque a API `https://cataas.com/cat` retorna **imagem binária** e não JSON.  
Ao trocar `data["message"]` por `data["url"]`, o código passou a tentar ler JSON de uma resposta que não era JSON, causando o `JSONDecodeError`.

### Como os testes ajudaram
- A suíte de **20 testes unitários** detectou imediatamente a falha (10 casos positivos e 10 negativos).  
- Os testes que esperavam a chave `"message"` no JSON quebraram.  
- Isso evidenciou a regressão e provou que os testes cumprem seu papel.

### Correção
A correção foi **voltar o código original**:

```python
data = response.json()
return data["message"]

