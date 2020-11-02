## 📚  Descrição 

Aplicação consiste em receber 1 ou mais contatos de celulares através de uma API Rest e adicioná-los ao banco de dados do cliente Macapá ou do cliente Varejão.:

## Regras
Fluxo de Ações
- A API receberá um JSON via POST contendo o nome e celular;
- O cliente deverá estar autenticado para inserir o contato na base
- O contato deverá ser inserido no banco de dados do cliente seguindo as regras de cada cliente

Especificações da API:
- A autenticação será através de um token JWT no Authorization Header
- Cada cliente tem 1 uma chave única
- A lista de contatos que será inserido em cada cliente está no arquivo contato.json

Especificações do Cliente Macapá:
- Banco de dados Mysql
- Formato do Nome é somente maiúsculas
- O formato de telefone segue o padrão +55 (41) 93030-6905
- Em anexo está o sql de criação da tabela

Especificações do Cliente Varejão:
- Banco de dados Postgresql
- Formato do Nome é livre
- O formato de telefone segue o padrão 554130306905
- Em anexo está o sql de criação da tabela

Exemplo de arquivo JSON recebido via POST:
```
{
    "contacts": [
        {
            "name": "Marina Rodrigues",
            "cellphone": "5541996941919"
        },
        {
            "name": "Nicolas Rodrigues",
            "cellphone": "5541954122723"
        },
        {
            "name": "Davi Lucca Rocha",
            "cellphone": "5541979210400"
        },
        {
            "name": "Sr. Marcos Vinicius Duarte",
            "cellphone": "5541979767374"
        }
    ]
}
```

## 🚀 Tecnologias Usadas 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">

<img src="https://user-images.githubusercontent.com/64918635/93954857-ddcbea80-fd24-11ea-89a8-213950b038ca.png" width = "150">

<img src="https://user-images.githubusercontent.com/64918635/95004996-1db68b80-05c9-11eb-8703-b42642372bd5.png" width = "150">

<img src="https://user-images.githubusercontent.com/64918635/97925563-62585280-1d40-11eb-82e6-7178c59fc19d.png" width = "150">

Desenvolvido em Python 3.8.0 <br>
SO utilizado: Windows 10 <br>
IDE utilizada: VSCode <br>

## 📌 Estrutura do Projeto 
    |-- macapa
       |-- create-table-macapa.sql
    |-- varejao
       |-- create-table-varejao.sql
    |-- collection.json
    |-- contacts-macapa.json    
    |-- contacts-varejao.json    
    |-- docker-compose.yml
    |-- main.py
    |-- README.md
    |-- requirements.txt 

pastas macapa e varejao -> pastas contendo os arquivos sql com as instruções para a criação das tabelas nos bancos de dados.

collection.json -> Arquivo contendo o exemplo da requisição à ser importado em um programa de requisições como o POSTMAN ou INSOMNIA.

contacts-macapa.json e contacts-varejao.json -> arquivos a serem importados para os bancos de dados via POST

docker-compose.yml -> Arquivo contendo instruções para o Docker. 

main.py -> Arquivo principal que contém a execução do projeto.

requirements.txt -> Bibliotecas utilizadas no python 

## 📢 Como executar

Requisitos:

Python 3.8.0<br>

Instalar todas as dependências do python usando o arquivo requirements.txt que está no projeto:  

```bash 
pip install  -r requirements.txt
 ```  
Ao executar o comando acima, será feita a instalação das seguintes bibliotecas:

```
cffi==1.14.3
click==7.1.2
cryptography==3.2.1
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
jwt==1.1.0
MarkupSafe==1.1.1
psycopg2==2.8.6
pycparser==2.20
PyJWT==1.7.1
PyMySQL==0.10.1
six==1.15.0
Werkzeug==1.0.1
```

Executar o main.py no cmd com o comando:

```bash 
python main.py
```  
Ao executar o comando, deverá aparecer a seguinte mensagem: Running on http://127.0.0.1:5000/ (Press CTRL+C to quit), conforme imagem abaixo.

<img src="https://user-images.githubusercontent.com/64918635/97925803-c549e980-1d40-11eb-9ec1-699895970fec.png">

Acessando o link com o endpoint http://127.0.0.1:5000/login, deverá aparecer a tela de login

<img src="https://user-images.githubusercontent.com/64918635/97925957-0c37df00-1d41-11eb-860d-4d12d122650b.png">
Ao acessar com o login e senha de cada cliente:

```bash
Nome de usuário: macapa
Senha: senhamacapa
```

ou

```bash
Nome de usuário: varejao
Senha: senhavarejao
```

deverá aparecer a tela de acesso concedido com o nome do usuário e o token a ser utilizado para validação de envio do JSON ao banco de dados via POST
<img src="https://user-images.githubusercontent.com/64918635/97925990-1eb21880-1d41-11eb-84fe-9fda7812c563.png">

Acessando o link com http://127.0.0.1:5000/protected?token=<token_gerado_aqui>, poderá verificar se o token é válido
<img src="https://user-images.githubusercontent.com/64918635/97926092-4d2ff380-1d41-11eb-9211-3d14afd50b68.png">

Esse mesmo token deverá ser informado para a validação de envio do JSON ao banco de dados via POST.<br>
Importar o arquivo collection.JSON utilizando um programa de requisições REST, como o <a href="https://insomnia.rest/download/">Insomnia</a> ou o <a href="https://www.postman.com/downloads/">Postman<a> e informar o IP: http://127.0.0.1:5000/protected?token=<token_gerado_aqui>, preenchendo o body no formato JSON, ou copiar e colar o arquivo contacts-macapa.json ou contacts-varejao.json disponível no repositório, conforme abaixo:
  
<img src="https://user-images.githubusercontent.com/64918635/97925721-a64b5780-1d40-11eb-8bbd-d58b4ed3c675.png">

Abaixo seguem os resultados obtidos nos bancos de dados, ressaltando que ao executar a requisição POST com o token informado, o token gerado para o cliente Macapá enviará as informações do JSON para o banco de dados MySQL e o token gerado para o cliente Varejão enviará o JSON para o banco de dados PostgreSQL conforme imagens abaixo, seguindo a formatação desejada para cada banco.

Banco de dados MySQL:
<img src="https://user-images.githubusercontent.com/64918635/97925696-9c295900-1d40-11eb-8968-9f544b9bbd1c.png">

Para o banco de dados no PostgreSQL houve um pouco mais de dificuldade, devendo ser executado no pgAdmin o comando abaixo para liberar o acesso ao banco via requisição POST:

```bash
GRANT ALL PRIVILEGES ON TABLE contacts TO admin;
GRANT USAGE, SELECT ON SEQUENCE contacts_id_seq TO admin;
```

Banco de dados PostgreSQL:
<img src="https://user-images.githubusercontent.com/64918635/97925851-deeb3100-1d40-11eb-98c3-69d9fd77192c.png">

## 🔓 Licença 
MIT © [Matheus Muller](https://www.linkedin.com/in/matheus-herrera-bezerra-muller/)
