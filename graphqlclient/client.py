import urllib
import json

class GraphQLClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token):
        self.token = token

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        if self.token is not None:
            headers['Authorization'] = 'Bearer %s' % self.token

        req = urllib.request(self.endpoint, json.dumps(data), headers)

        try:
            response = urllib.request.urlopen(req)
            return response.read()
        except urllib.error.HTTPError as e:
            print((e.read()))
            print('')
            raise e
