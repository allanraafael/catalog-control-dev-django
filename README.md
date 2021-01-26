# Dev Django

## Para executar o projeto realize as orientações a seguir:

### Instale as dependências

>#### Crie uma virtualenv, ative-a e instale as dependências, pode ser virtualenv, pipenv, poetry, como você preferir.

#### Instale o pipenv um dos gerenciadores de pacotes mais utilizados para instalação de dependências 
```shell script 
> pipenv install
```

ou
#### Caso preferir instale as dependências no seu ambiente virtual pelo próprio pip do arquivo requirements.txt
```shell script 
> pip install -r requirements.txt
```

### Variáveis de ambiente
##### Essas variáveis são carregadas pela configuração principal do projeto que é a pasta config
#### 1. Crie uma cópia do arquivo `.env.example` (que está raiz do projeto) e o renomeie para `.env`, com o comando: 

```shell script 
>    cp .env.example .env
```

#### 2. Altere o arquivo `.env`, definindo as variáveis de ambiente necessárias para o projeto funcionar corretamente
#### configurações de banco de dados, senhas, chave de API, etc...

>#### OBS: Em produção também é utilizado esse modelo de arquivo`.env`, porém de acordo com as configurações corretas para o ambiente de produção
>
> #### Ex: DEBUG = False
