#!/usr/bin/env python

from graphqlclient import GraphQLClient

def main():
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

if __name__ == '__main__':
    main()
