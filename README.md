# PROJECT FLASK

## Projeto de microblog utilizando o (micro)framework Python Flask

## Executanto o projeto

### 1. Instalando o interpretador Python e o gerenciador de pacotes 'pip'
Para executar o programa, primerio você precisa ter um interpretador Python instalado em seu computador, além do grenciador de pacotes 'pip'.
Primeiro, instale o python 3 em seu computador. Para isso, acesse o site oficial do python e baixe a versão mais recente do interpretador. Ou, se preferir, use o comando, caso esteja usando o linux ubuntu:

```bash
sudo apt-get install python3
```

No Windows, acesse o site oficial do python e baixe a versão mais recente do interpretador.
Após a instalação, verifique se o python foi instalado corretamente, digitando o comando:

```bash
python --version
```

ou

```bash
python3 --version
```

Caso a versão do python seja exibida, o interpretador foi instalado corretamente.

### 2. Instale o gerenciador de pacotes 'pip' em seu computador.

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

### 3. Criando ambiente virtual

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

### 4. Instale todos os pacotes necessários:

Instale os pacotes necessários com o comando:

```bash	
pip install -r req.txt
```

### 5. Executando o projeto:

Para executar o projeto, primeiro é preciso que você crie as variáveis de ambiente. Para isso, use o comando:

```bash
export FLASK_APP=App.py
```

Em seguida, você poderá executar o projeto com o comando:

```bash
flask run
```

### REFERÊNCIAS

- [The Flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
