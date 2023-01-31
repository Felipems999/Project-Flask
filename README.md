# PROJETO MICROBLOG

## Projeto de microblog utilizando o (micro)framework Python Flask

### Executanto o projeto
#####    1. Para executar o programa, primerio você precisa ter um interpretador Python instalado em seu computador, além do grenciador de pacotes 'pip'. Tendo estes requisitos, clone o repositório e crie um ambiente virtual com o comando: 
    - 'python -m venv <nome do ambiente'; 
    - ou 'python3 -m venv <nome do ambiente>'. 

#####    2. Para executá-lo, use o comando:
    - 'source venv/bin/activate', no linux;
    - 'venv/Scripts/activate.bat', no MS Windows;
    - ou 'venv/Scripts/Activate.ps1' no VSCode.

#####    3. Instale todos os pacotes necessários para que a webapp deste projeto funcione corretamente usando o comando:
    - 'pip install -r req.txt'.
    
#####    4. Para executar o projeto, basta usar o comando:
    - 'flask run'.

### Sobre o microblog
#####    O microblog possui, até o momento, 4 diferentes rotas(páginas): '/index', '/login', '/contato' e '/about'. A rota '/index' leva até a home page, onde são exibidos posts, e cada post contem informações como: autor do post, texto do post e data de publicação, além de um mensagem de boas vindas. A rota '/login' redireciona o usuário á pagina que contêm o formulário de login. Os campos 'Username' e 'Password' são obrigatórios, enquato o campo 'Lembrar de mim' é opcional. Caso tenha sucesso na validação, o usuário é redirecionado à Home, onde a mensagem 'Requisição de login para {form.username.data}, remember_me = {form.remember_me.data}' é exibida, com os campos em '{{}}' devidamente preenchidos. A página da rota '/contato' também possui um formulário, com os campos 'Email' e 'Text', ambos obrigatórios. Ao preechê-los e clicar no botão 'Enviar', o usuário é redirecionado para esta mesma página, onde os 2 campos estarão limpos. Por fim, na página 'Sobre'(rota '/about'), caso o parâmetro esteja vazio, uma mensagem pré-determinada será exibida, mas caso o parâmetro 'description' tenha sido passado com alguma string, no retorno do método 'about', essa string será exibida.

### REFERÊNCIA

- [The Flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
