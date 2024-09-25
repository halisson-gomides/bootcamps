## Farol na quebrada 
<img src="img/logo_farol_na_quebrada.jpg" style="width:150px; height:130px">

### Aula extra de python 
Exploraremos um pouco mais o poder da [linguagem de programação mais utilizada no mundo atualmente](https://spectrum.ieee.org/top-programming-languages-2024).

#### Quem é o professor:

- [![Link](https://img.shields.io/badge/GITHUB%20PAGE-Halisson%20Gomides-D3D33?style=flat&logo=github&logoColor=black)](https://halisson-gomides.github.io/)

#### Começando do começo
1. Instalar o [python](http://python.org)
2. Criar um repositório no [GitHub](https://github.com/)
3. Instalar uma IDE de desenvolvimento 

|Vs Code|PyCharm|
|:-:|:-:|
|[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/Download)|[![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)](https://www.jetbrains.com/pt-br/pycharm/download/?section=windows)|

4. Criar um diretório onde ficará os arquivos fonte do projeto
5. Clonar o repositório criado no GitHub dentro do diretório criado: 
    - `git clone https://github.com/<usuario_git>/<nome_repositorio>.git .`
6. Criar um [ambiente virtual python](https://docs.python.org/pt-br/3/library/venv.html) dentro do diretório.
    - `python -m venv ./env_farol`
7. Ativar o ambiente virtual criado:
    - `env_farol\Scripts\activate`
8. Instalar bibliotecas que serão utilizandas no projeto
    - `python -m pip install --upgrade pip`
    - `pip install <nome_biblioteca1> <nome_biblioteca2> ...`
9. Criar o arquivo `.gitignore` na raiz do diretório criado e adicionar:
    - `env_farol/`