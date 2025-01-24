import os
import subprocess
import argparse
from .utils import ContexDirectory

def create(project_name: str,
           path: str='.',
           requirements: str='.') -> None:
    """
    Description:
    ------------
        This function creates a new poetry project and installs the required dependencies.
    
    Args:
    -----
        project_name -- the name of the project to be created
    
    Returns:
    --------
        None
    """
    with ContexDirectory(path):
        if project_name is None:
            raise ValueError('Project name is required!')
        # 1.0 Activate the virtual environment and then install poetry
        subprocess.Popen(['python', '-m', 'pip', 'install', 'poetry']).wait()
        # 2.0 Create a new poetry project
        subprocess.Popen(['poetry', 'new', project_name]).wait()
        # 3.0 Move into the project directory to install the dependencies
        try:
            os.chdir(project_name)
        except FileNotFoundError:
            print('Directory not found!')
            return  # Return control to the main process
        # 4.0 Install the required dependencies
        subprocess.Popen(['poetry', 'add', 'sphinx']).wait()
        subprocess.Popen(['poetry', 'install']).wait()
        # Check if requirements.txt file exists
        if os.path.isfile(requirements):
            # take all the packages from the requirements.txt and install it to the virtual environment
            with open(requirements, 'r') as f:
                for line in f:
                    subprocess.Popen(['poetry', 'add', line.strip()]).wait()

            subprocess.Popen(['poetry', 'install']).wait()

            print('Dependency added and installed!')
        else:
            print('requirements.txt file not found!')
        # 5.0 Create the sphinx documentation
        subprocess.Popen(['sphinx-quickstart',
                        '-q',
                        '-p',f'{project_name}',
                        '-a', 'Author',
                        '-v', '1.0',
                        '-d', 'docs',
                        '-r', '1.0',
                        '-l', 'en',
                        '--sep']).wait()
        print('Dependency added and installed!')
        # Return control to the main process


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Setup poetry project.')
    parser.add_argument('-p', '--project_name', type=str, help='The name of the project')
    parser.add_argument('-d', '--path', type=str, help='The path of the project')
    parser.add_argument('-r', '--requirements', type=str, help='The path of the requirements file')
    args = parser.parse_args()
    create(project_name=args.project_name, 
           path=args.path,
           requirements=args.requirements)