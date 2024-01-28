# PROJETO MICROBLOG

## Projeto de microblog utilizando o (micro)framework Python Flask

### 1- Executanto o projeto
##### Para executar o programa, primerio você precisa ter um interpretador Python instalado em seu computador, além do grenciador de pacotes 'pip'.

Primeiro, instale o python 3 em seu computador. Para isso, acesse o site oficial do python e baixe a versão mais recente do interpretador. Ou, se preferir, use o comando, caso esteja usando o linux ubuntu:

```bash
sudo apt-get install python3
```

Após a instalação, verifique se o python foi instalado corretamente, digitando o comando:

```bash
python --version
```

ou

```bash
python3 --version
```

Caso a versão do python seja exibida, o interpretador foi instalado corretamente.

#####    2. Instale o gerenciador de pacotes 'pip' em seu computador.

Para isso, acesse o site oficial do python e baixe a versão mais recente do gerenciador. Ou, se preferir, use o comando, caso esteja usando o linux ubuntu:

```bash
sudo apt-get install python3-pip
```

Após a instalação, verifique se o pip foi instalado corretamente, digitando o comando:

```bash
pip --version
```

ou

```bash
pip3 --version
```

Caso a versão do pip seja exibida, o gerenciador de pacotes foi instalado corretamente.

#####    3. Criando ambiente virtual

Clone o projeto em seu computador, usando o comando:

```bash
git clone https://github.com/Felipems999/Project-Flask.git
```

Após clonar o projeto, acesse a pasta do projeto e crie um ambiente virtual.

```bash
cd Project-Flask
```

Para criar um ambiente virtual, você precisa instalar o pacote 'venv'. Para isso, use o comando:

```bash
sudo apt-get install python3-venv
```

Após a instalação, crie o ambiente virtual usando o comando:

```bash
python -m venv <nome do ambiente> 
```

ou 

```bash
python3 -m venv <nome do ambiente>
```

Para executá-lo, use o comando:

- No linux ubuntu:

```bash	
source venv/bin/activate
```

- No Windows:
```bash	
venv/Scripts/activate.bat
```

ou, caso esteja usando o powershell:

```bash	
venv/Scripts/Activate.ps1
```

#####    4. Instale todos os pacotes necessários:

Instale os pacotes necessários com o comando:

```bash	
pip install -r req.txt
```

#####    5. Executando o projeto:

Para executar o projeto, primeiro é preciso que você crie as variáveis de ambiente. Para isso, use o comando:

```bash
export FLASK_APP=App.py
```

Em seguida, você poderá executar o projeto com o comando:

```bash
flask run
```

### Sobre o microblog
#####    O microblog possui, até o momento, 4 diferentes rotas(páginas): '/index', '/login', '/contato' e '/about'. A rota '/index' leva até a home page, onde são exibidos posts, e cada post contem informações como: autor do post, texto do post e data de publicação, além de um mensagem de boas vindas. A rota '/login' redireciona o usuário á pagina que contêm o formulário de login. Os campos 'Username' e 'Password' são obrigatórios, enquato o campo 'Lembrar de mim' é opcional. Caso tenha sucesso na validação, o usuário é redirecionado à Home, onde a mensagem 'Requisição de login para {form.username.data}, remember_me = {form.remember_me.data}' é exibida, com os campos em '{{}}' devidamente preenchidos. A página da rota '/contato' também possui um formulário, com os campos 'Email' e 'Text', ambos obrigatórios. Ao preechê-los e clicar no botão 'Enviar', o usuário é redirecionado para esta mesma página, onde os 2 campos estarão limpos. Por fim, na página 'Sobre'(rota '/about'), caso o parâmetro esteja vazio, uma mensagem pré-determinada será exibida, mas caso o parâmetro 'description' tenha sido passado com alguma string, no retorno do método 'about', essa string será exibida.

### REFERÊNCIA

- [The Flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
