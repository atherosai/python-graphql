
## Technologies

- Python
- Flask - minimalistic server framework for Python
- GraphQL - Query language and API technology
- GUnicorn - WSGI server for production environments
- NLTK - Natural Language processing toolkit

## Development

After cloning the repository just navigate into the folder. Assuming that you have installed the newest Python and Pipenv you should be able to execute:

```
pipenv shell
```

This creates virtual environment for your application. Then we can install modules with:

```
pipenv install
```

For development mode you can run

```
pipenv run dev
```

Then for production mode and the use of WSGI server you should run

```
pipenv run prod
```

Both applications are run on common port **5000** for Flask applications. Documentation is available at http://localhost:5000/graphiql.

# This repository demonstrates the code for the following articles
* https://atheros.ai/blog/how-to-build-graphql-api-for-text-analytics-in-python
* https://atheros.ai/blog/text-classification-with-transformers-in-tensorflow-2