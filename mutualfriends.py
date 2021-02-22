import requests

token = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'

class VkUser:

    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token' : self.token,
            'v' : self.version
        }
        self.owner_id = requests.get(self.url + 'users.get', self.params).json()['response'][0]['id']

    def friends_get (self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        friends_url = self.url + 'friends.get'
        friends_params = {
            'count' : 1000,
            'user_id' : user_id
        }
        resp = requests.get(friends_url, params={**self.params, **friends_params})
        return resp.json()

vk_client = VkUser(token, 5.21)

print(set(vk_client.friends_get(147633933)['response']['items']) & set(vk_client.friends_get(56)['response']['items']))

