# Image Cross-Correlation (ICC)
-----------------------------------------

- Author: Baljyot Singh Parmar
- Affiliation at the time of writing: McGill University, Canada. Weber Lab



## 1. Installation
-------------------
1. Make sure you have anaconda installed: <https://www.anaconda.com/download>
2. Download or clone this repository.
3. In the conda prompt, navigate to the folder where you downloaded this repository using : **cd "path_to_folder"**
4. Using the **ICC.yml** file, create a new environment using: **conda env create -f ICC.yml**
    - If you get an environment resolve error but you have anaconda installed just skip to step 6. The .yml file is for people who are using miniconda and might not have the packages already installed with the full anaconda install.
    - You may want to still have a conda environment so just create a generic one if you want with the name ICC or whatever you want with python>=3.10. Explicitly, **conda create -n [my_env_name] python=3.10**.
5. Activate the environment using: **conda activate ICC**
6. Now we will install this package in edit mode so we can use its functionalities without invoking sys.path.append() every time.
    - Run the command: **pip install -e . --config-settings editable_mode=compat**
    - This will install the package in editable mode and you can now use the package in any python environment without having to append the path every time. 
7. Read the walkthrough. TODO: add a text file with the walkthrough to explain math and code.
