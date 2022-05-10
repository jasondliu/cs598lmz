import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

# In[ ]:


# Uninstall helper in case you need to uninstall fastai
def uninstall_fastai_packages(our_system='cpu'):
    if our_system == 'cpu':
        !pip uninstall fastai -y
    else:
        !pip uninstall torch torchvision fastai -y
        !pip install -r {repo_path}/requirements/requirements-colab.txt
        !pip install {repo_path} --upgrade
try:
    if ctypes.windll.shell32.IsUserAnAdmin():
        if sys.version_info >= (3,8):
            print('win32 found, not uninstalling in case you want it')
        else:
            print(ctypes.windll.shell32.IsUserAnAdmin())
            print('You are a superuser')
            #uninstall_fastai_packages('cpu') # Change parameter to 'gpu' if available
    else:
        print('You are not superuser')
        print(ctypes.windll.
