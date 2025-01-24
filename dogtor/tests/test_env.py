import os
from dogtor.env import create

def test_create_env():
    env_name = 'test_env'
    create(env_name)
    assert os.path.exists(env_name)
    os.system(f'rm -rf {env_name}')

def test_create_env_with_default_name():
    create()
    assert os.path.exists('project_env')
    os.system('rm -rf project_env')