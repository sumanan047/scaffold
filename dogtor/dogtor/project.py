import os
import subprocess
import argparse


def create(project_name: str) -> None:
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
    parent_dir = os.path.dirname(os.getcwd())
    if os.path.isfile(os.path.join(parent_dir, 'requirements.txt')):
        # take all the packages from the requirements.txt and install it to the virtual environment
        with open(os.path.join(parent_dir, 'requirements.txt'), 'r') as f:
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
    exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Setup poetry project.')
    parser.add_argument('-p', '--project_name', type=str, help='The name of the project')
    args = parser.parse_args()
    create(project_name=args.project_name)