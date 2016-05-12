#!/usr/bin/env python

from graphqlclient import GraphQLClient

def main():
    client = GraphQLClient('http://graphql-swapi.parseapp.com/')

    print(client.execute('''
    {
      allFilms {
        films {
          title
        }
      }
    }
        '''))

if __name__ == '__main__':
    main()
