# Histórico de Desenvolvimento

## O Problema:
O desafio consistia na implantação da aplicação de Comentários em versão API (backend) utilizando ferramentas open source de preferência do desenvolvedor. O objetivo era criar um ambiente de execução para esta API com o máximo de automação possível, incluindo a criação da esteira de deploy.

A aplicação seria uma API REST disponível neste repositório, permitindo aos usuários enviar comentários sobre uma matéria e visualizar os comentários de outros usuários sobre o mesmo assunto.

### Ideias Iniciais:
- Utilização do GitHub Actions para integração contínua.
- Adoção de um modelo de pastas específico.
- Criação de testes unitários.
- Execução dos testes antes do build/deploy.

## Início:
- Construção da estrutura de pastas.
- Problemas com o provisionamento da infraestrutura usando Terraform.
- Problemas de permissões ao enviar imagens Docker para a EC2.

## Desenvolvimento e Testes:
- Criação de testes unitários para api.py.
- Implementação de uma task de teste no GitHub Actions.
- Problemas na subida da imagem Docker e na estrutura de pastas.

## Ajustes Finais e Conclusão:
- Centralização dos arquivos na pasta app.
- Finalização do projeto com endpoints funcionais.
  
### Ideias de Melhorias:
- Criação de um ECS com IP e instâncias fixos.
- Utilização do S3 para armazenar as imagens diretamente.

