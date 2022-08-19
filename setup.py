# setup.py 파일이 있으면 pip로 설치 가능하다.
from setuptools import setup

setup(
    name='myapi', #  이 이름으로 패키지가 설치
    version= '0.0.1',
    description= 'my api lib',
    url= 'https://github.com/beon0/api_project.git',
    author= 'hyunji',
    author_email= 'rlaguswl706926@naver.com',
    package= ['my_api'],
    zip_safe = False,
    install_requires = [
        'requests'
    ]
)