# Sistema de Gerenciamento de Cadastros

Este repositório contém um sistema simples, porém funcional, de gerenciamento de cadastros implementado em Python com o uso do SQLite. Se o banco de dados não for encontrado, o programa automaticamente criará o banco com as tabelas necessárias para o funcionamento do sistema.

## Sobre o Sistema

O sistema permite realizar operações básicas de um CRUD (Create, Read, Update, Delete), como inserir, listar, atualizar e excluir cadastros no banco de dados. É uma ferramenta útil para gerenciar informações de cadastro como nome, email e cargo de indivíduos.

## Pré-Requisitos

Para executar este sistema, você precisará ter o Python instalado em seu computador. O SQLite é embutido no Python, então não é necessário instalá-lo separadamente.

## Como Usar

1. Clone este repositório ou baixe o arquivo `.py` para o seu computador.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo foi salvo.
4. Execute o script com o comando `python nome_do_arquivo.py`.
5. O menu do sistema será exibido. Siga as instruções na tela para interagir com o sistema.

## Recursos

- **Inserir Cadastro**: Permite adicionar novos cadastros ao banco de dados.
- **Listar Cadastros**: Exibe todos os cadastros presentes no banco de dados.
- **Atualizar Cadastro**: Permite modificar as informações de um cadastro existente.
- **Excluir Cadastro**: Remove um cadastro do banco de dados.
- **Sistema Auto-Suficiente**: Cria o banco de dados e a tabela necessária automaticamente, se não existirem.

## Estrutura do Banco de Dados

O banco de dados utiliza a seguinte estrutura de tabela para armazenar os cadastros:
tb_cadastro:
* id (INTEGER): Chave primária, autoincremento
* nome (TEXT): Nome do indivíduo
* email (TEXT): Endereço de email
* cargo (TEXT): Cargo ocupado pelo indivíduo

## Conclusões

Este sistema de gerenciamento de cadastros é uma excelente ferramenta para quem precisa de uma solução simples e eficaz para gerenciar informações de cadastro. Sua capacidade de autoconfiguração e a simplicidade da interface de usuário tornam-no acessível até mesmo para usuários sem experiência em programação ou gerenciamento de banco de dados.

### Reflexão:
>"A mente que se abre a uma nova ideia jamais voltará ao seu tamanho original.
>O aprendizado expande nossos horizontes, transforma nossa perspectiva e enriquece nossa jornada,
>tornando-nos eternos aprendizes no vasto mundo do conhecimento."
