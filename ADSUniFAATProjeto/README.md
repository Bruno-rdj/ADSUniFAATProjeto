# ADSUniFAATProjeto - Implementação de Servidores

Este repositório foi desenvolvido para a disciplina de **Implementação de Servidores** do curso de **Análise e Desenvolvimento de Sistemas (A.D.S)** da **Unifaat**. O objetivo deste projeto foi criar uma infraestrutura de servidor que envolva o uso de **Docker**, **PostgreSQL** e a construção de um banco de dados para gerenciar as informações de uma escola fictícia.

## Estrutura do Banco de Dados

O banco de dados `Escola` contém as seguintes tabelas:

- **Professor**: Tabela responsável por armazenar os dados principais dos professores, como nome, e-mail e telefone.
- **Turma**: Armazena informações sobre as turmas, como o nome da turma, o horário das aulas e o professor responsável por ela.
- **Aluno**: Contém os dados dos alunos, como nome, data de nascimento, dados de contato e a turma à qual eles pertencem.

### Relacionamentos Entre as Tabelas

- **Aluno e Turma**: Cada aluno pertence a uma turma, e uma turma pode ter vários alunos. Esse relacionamento é feito através da chave estrangeira `id_turma` na tabela `Aluno`, que faz referência ao campo `id_turma` da tabela `Turma`.
- **Turma e Professor**: Cada turma é associada a um único professor, mas um professor pode ser responsável por várias turmas. A chave estrangeira `id_professor` na tabela `Turma` estabelece esse vínculo com a tabela `Professor`.
