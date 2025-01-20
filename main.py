import os
import subprocess
import argparse


def main(project_name, debug=True):
    # Activate the virtual environment and then install poetry
    subprocess.Popen(['python', '-m', 'pip', 'install', 'poetry']).wait()

    print('Poetry installed!')

    if not debug:
        return
    else:
        # Print the pip list
        subprocess.Popen(['pip', 'list'])

    # Create a new poetry project
    subprocess.Popen(['poetry', 'new', project_name]).wait()

    print('Poetry project created!')

    # Change the directory to the project directory and list the files
    try:
        os.chdir(project_name)
    except FileNotFoundError:
        print('Directory not found!')
        return  # Return control to the main process

    print('Directory changed and files listed!')


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

    # Move into the directory project_name and start the sphinx project
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
    parser.add_argument('project_name', type=str, help='The name of the project')
    args = parser.parse_args()
    main(project_name=args.project_name)