# python-graphql-client
Simple GraphQL client for Python 2.7+

## Install

```sh
pip install graphqlclient
```

## Usage


```py
from graphqlclient import GraphQLClient

client = GraphQLClient('http://graphql-swapi.parseapp.com/')

result = client.execute('''
{
  allFilms {
    films {
      title
    }
  }
}
''')

print(result)
```

### Authorization

Authorization tokens can be added to the request using the client's `inject_token` method:

```
client.inject_token('very-long-and-secure-token')
```

## License

[MIT License](http://opensource.org/licenses/MIT)
