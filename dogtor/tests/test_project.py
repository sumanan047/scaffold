import os
from dogtor.project import create

def test_create_project():
    project_name = 'test_project'
    create(project_name, 
           path='.',
           requirements=r'/Users/sudofr/Documents/Projects/Coding/piatos/scaffold/requirements.txt')
    assert os.path.exists(project_name)
    os.system(f'rm -rf {project_name}')

def test_create_project_no_requirements():
    project_name = 'test_project'
    create(project_name, 
           path='.')
    assert os.path.exists(project_name)
    os.system(f'rm -rf {project_name}')