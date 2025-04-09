# ADSUniFAATProjeto - Implementação de Servidores

Este repositório foi desenvolvido para a disciplina de **Implementação de Servidores** do curso de **Análise e Desenvolvimento de Sistemas (ADS)** da **Unifaat**. O objetivo deste projeto foi criar uma infraestrutura de servidor que envolva o uso de **Docker**, **PostgreSQL** e a construção de um banco de dados para gerenciar as informações de uma escola fictícia.

## Estrutura do Banco de Dados

O banco de dados `Escola` contém as seguintes tabelas:

- **Professor**: Tabela responsável por armazenar dados dos professores, como nome, e-mail e telefone.
- **Turma**: Armazena informações sobre as turmas, como o nome da turma, o horário das aulas e qual professor é responsável por ela.
- **Aluno**: Contém os dados dos alunos, como nome, data de nascimento, dados de contato e a turma à qual eles pertencem.

### Relacionamentos Entre as Tabelas

- **Aluno e Turma**: Cada aluno pertence a uma turma, e uma turma pode ter vários alunos. Esse relacionamento é feito através da chave estrangeira `id_turma` na tabela `Aluno`, que referencia o campo `id_turma` da tabela `Turma`.
- **Turma e Professor**: Cada turma é associada a um único professor, mas um professor pode ser responsável por várias turmas. A chave estrangeira `id_professor` na tabela `Turma` faz esse vínculo com a tabela `Professor`.

### Pré-Requisitos
Para rodar essa aplicação, precisa ter algumas ferramentas instaladas na máquina:

• Docker Engine

• Docker-Compose

• Editor de Código de sua preferência

Docker-Compose


### Siga o passos a seguir para rodar o Docker-Compose:

Primeiro certifique-se de que você tem o Docker e o Docker-Compose instalados na sua máquina.
   ```bash
   docker --version

   docker-compose --version
   ```

   Execute o comando para iniciar os contêineres com o Docker-Compose:
   ```bash
   docker-compose up --build
   ```

Caso precise parar ou remover contêineres, execute o seguinte comando no diretório raiz:
   ```bash
docker-compose down
   ```

## Instruções para Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Bruno-rdj/ADSUniFAATProjeto.git

   cd ADSUniFAATProjeto/DB
      ```
