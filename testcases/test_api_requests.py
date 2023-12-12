import pytest 
import os
import requests
from common import load_file

class TestApi:
    s = requests.session()

    # def test_user_users(self):
    #     result = self.s.get('http://172.17.0.1:4000/user/users')
    #     print(result.json())


    # # @pytest.mark.skip()
    # @pytest.mark.parametrize(
    #     'data',
    #     load_file.load_yaml(os.path.join(os.path.dirname(__file__),'../data/data.yaml'))
    #     )
    # def test_user_create(self,data):
    #     result = self.s.post(
    #         url='http://172.17.0.1:4000/user/users',
    #         json=data
    #     )
    #     print(result.json())
    def test_example(self):
        res = self.s.get("https://example.com")
        assert res.status_code == 200








if __name__ == '__main__':
    s = requests.session()
    result = s.get('http://127.0.0.1:4000/user/users')
    print(result.json())
    