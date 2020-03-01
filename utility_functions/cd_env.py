
import sys

def cd_env(folder='ds_Projects',project=None, mod=None, env=None, envname=None):
    """
    Function to get a project's working directory and associated virtul environmentself.
    :folder: use if there's a folder between the root and project directory
             default = 'ds_Projects'
    :project: name of project folder; default=None
       :mod: module name; applicable for standard 'cookiecutter' templates
    :env: management system (conda, virtualenv, cc); default=None
    :envname: name of virtual environment; default=None  
    """
    cd = f"cd ~/{folder}/{project}"
    cd_ccpy = f"cd ~/{folder}/{project}/{mod}"
    activ_ccpy= f"source .virtualenvs/{envname}/Scripts/activate"
    activ_conda= f"conda activate {envname}"
    if env == 'conda':
        print(cd)
        print(activ_conda)
    elif env=='cc':
        print(f"cd ~/{folder}/{project}/src/{mod}")
        print(f'source activate {envname}')
        print("\n- Based on 'standard cookiecutter'")
    else:
        print(cd_ccpy)
        print(activ_ccpy)
        print("\n- Based on 'cookiecutter-pypackage'")


if __name__ == "__main__":
    cd_env(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])


