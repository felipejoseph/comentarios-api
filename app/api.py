from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

app_name = 'comentarios'
app = Flask(app_name)

comments = {}

# Definição das rotas da API
@app.route('/api/comment/new', methods=['POST'])
def api_comment_new():
    request_data = request.get_json()

    email = request_data['email']
    comment = request_data['comment']
    content_id = '{}'.format(request_data['content_id'])

    new_comment = {
            'email': email,
            'comment': comment,
            }

    if content_id in comments:
        comments[content_id].append(new_comment)
    else:
        comments[content_id] = [new_comment]

    message = 'comment created and associated with content_id {}'.format(content_id)
    response = {
            'status': 'SUCCESS',
            'message': message,
            }
    return jsonify(response)

@app.route('/api/comment/list/<content_id>')
def api_comment_list(content_id):
    content_id = '{}'.format(content_id)

    if content_id in comments:
        return jsonify(comments[content_id])
    else:
        message = 'content_id {} not found'.format(content_id)
        response = {
                'status': 'NOT-FOUND',
                'message': message,
                }
        return jsonify(response), 404

# Servindo a especificação Swagger
@app.route('/swagger/spec')
def spec():
    # Carregar o arquivo Swagger
    with open('swagger.yaml', 'r') as f:
        swagger_spec = yaml.safe_load(f)
    return jsonify(swagger_spec)

# Configurando a interface Swagger
SWAGGER_URL = '/api/docs'
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    '/swagger/spec',
    config={
        'app_name': "API de Comentários"
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)  # Definindo a porta como 8000
