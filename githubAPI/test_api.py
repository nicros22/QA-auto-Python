import os

import pytest
from curl_cffi import requests
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="module")
def github_api():
    class GitHubAPI:
        def __init__(self):
            self.username = os.getenv('GITHUB_USERNAME')
            self.token = os.getenv('GITHUB_TOKEN')
            self.repo_name = os.getenv('REPO_NAME')
            self.api_url = 'https://api.github.com'
            self.headers = {
                'Authorization': f'token {self.token}',
                'Accept': 'application/vnd.github.v3+json',
                'User-Agent': self.username
            }

        def create_repo(self):
            url = f'{self.api_url}/user/repos'
            data = {'name': self.repo_name,
                    'auto_init': True,
                    'private': False}
            response = requests.post(url, json=data, headers=self.headers)
            return response

        def check_repo(self):
            url = f'{self.api_url}/repos/{self.username}/{self.repo_name}'
            response = requests.get(url, headers=self.headers)
            return response

        def delete_repo(self):
            url = f'{self.api_url}/repos/{self.username}/{self.repo_name}'
            response = requests.delete(url, headers=self.headers)
            return response

    return GitHubAPI()


def test_create_repo(github_api):
    response = github_api.create_repo()
    print(response.text)
    assert response.status_code == 201, "Ошибка при создании репозитория"


def test_check_repo(github_api):
    response = github_api.check_repo()
    assert response.status_code == 200, "Не смог найти репозиторий"
    data = response.json()
    assert data['name'] == github_api.repo_name, "Имя репозитория не совпадает"


def test_delete_repo(github_api):
    response = github_api.delete_repo()
    assert response.status_code == 204, "Ошибка при удалении репозитория"


def test_repo_deleted(github_api):
    response = github_api.check_repo()
    assert response.status_code == 404, "Репозиторий существует после удаления"
