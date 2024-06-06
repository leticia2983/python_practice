Steps to install python virtual workspaces in Windows:
1. Install Virtualenv:
   pip install virtualenv
2. python -m venv project1
   creates a folder for virtual workspace
3. cd project1   # or       project1\Scripts\activate
4. Scripts\activate
5. deactivate ---------------------> to come out of the virtual workspace
Workspaces help us to install and use different packages for different environments as well as departments. for eg some application may need a specific version of a module and other applications use different. in such cases virtual workspaces allows us to do so for the different applications as per their requirement.

Steps to install python virtual workspaces in Linux/Mac:
1.pip3 install virtualenv
2.python3 -m venv .venv
3.Activate a virtual environment:
source .venv/bin/activate
4.Deactivate a virtual environment
deactivate
