# Projeto de Automação de Implantação de Comentários

Este projeto automatiza a implantação de uma aplicação de comentários em uma instância EC2 na AWS utilizando o Terraform e o Docker.

## Visão Geral

O projeto consiste em duas partes principais:

1. **Configuração da Infraestrutura com Terraform**: Utiliza o Terraform para criar uma instância EC2 na AWS, configurar o DNS no Route 53 e implantar a aplicação.

2. **Implantação da Aplicação com Docker**: Utiliza o Docker para construir e implantar a aplicação de comentários na instância EC2.

## Configuração

Antes de executar os workflows do GitHub Actions, é necessário configurar algumas variáveis de ambiente secretas no repositório:

- `AWS_ACCESS_KEY_ID`: O ID da chave de acesso da AWS com permissões para criar instâncias EC2.
- `AWS_SECRET_ACCESS_KEY`: A chave de acesso secreta correspondente.
- `AWS_PEM`: O conteúdo da chave PEM usada para autenticar na instância EC2 via SSH.

## Executando o Projeto

1. **Configuração Inicial**
   - Clone este repositório para o seu ambiente local.
   - Configure as variáveis de ambiente secretas mencionadas anteriormente no repositório GitHub.

2. **Executando o Workflow do Terraform**
   - Certifique-se de que as configurações no arquivo `terraform/main.tf` estejam corretas, incluindo as credenciais da AWS e a configuração da instância EC2.
   - Faça um push para a branch master ou crie um pull request para acionar o workflow do Terraform.

3. **Executando o Workflow do Docker**
   - Certifique-se de que a aplicação de comentários está configurada corretamente e os arquivos `Dockerfile` e `docker-compose.yml` estejam presentes no diretório raiz do projeto.
   - Faça um push para a branch master ou crie um pull request para acionar o workflow do Docker.

## Endpoints

Após a implantação bem-sucedida, a aplicação estará disponível nos seguintes endpoints:

- **URL Base:** `comentarios.felipestestes.net:8000`
- **Endpoint da API de Comentários:** `comentarios.felipestestes.net:8000/api/comment/list/1`

### Exemplo de Uso

Para criar e listar comentários por matéria, você pode usar os seguintes comandos de exemplo:

# matéria 1
curl -sv comentarios.felipestestes.net:8000/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"first post!","content_id":1}'
curl -sv comentarios.felipestestes.net:8000/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"ok, now I am gonna say something more useful","content_id":1}'
curl -sv comentarios.felipestestes.net:8000/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"bob@example.com","comment":"I agree","content_id":1}'

# matéria 2
curl -sv comentarios.felipestestes.net:8000/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"bob@example.com","comment":"I guess this is a good thing","content_id":2}'
curl -sv comentarios.felipestestes.net:8000/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"charlie@example.com","comment":"Indeed, dear Bob, I believe so as well","content_id":2}'
curl -sv comentarios.felipestestes.net:8000/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"eve@example.com","comment":"Nah, you both are wrong","content_id":2}'

# listagem matéria 1
curl -sv comentarios.felipestestes.net:8000/api/comment/list/1

# listagem matéria 2
curl -sv comentarios.felipestestes.net:8000/api/comment/list/2
