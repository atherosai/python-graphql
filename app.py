from flask import Flask, request
from graphql_server.flask import GraphQLView
from server.schema.Schema import Schema

app = Flask(__name__, static_url_path='', template_folder='./public', static_folder='./public')


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.errorhandler(404)
@app.route("/404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/500")
def requests_error(error):
    return app.send_static_file('500.html')

#point GraphQL playground to /graphql endpoint

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
    'graphql',
    schema=Schema,
    #pass request to context to perform resolver validation
    get_context=lambda: {'request': request}
))

@app.route('/graphiql')
def playground_render():
    return app.send_static_file('playground.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')