from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
```

The data can be decompressed as follows:

```python
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
```

# How to create a virtual environment

```
sudo apt install python3-pip
pip3 install virtualenv
virtualenv -p python3 venv
```

To activate the newly created environment, execute:

```
source venv/bin/activate
```

To deactivate the environment, execute:

```
deactivate
```

To install all dependencies, execute:

```
pip install -r requirements.txt
```

To install a new package, execute:

```
pip install <package-name>
```

To freeze the currently installed packages, execute:

```
pip freeze > requirements.txt
```

# How to use a virtual environment in PyCharm

Click on **File** > **Settings** > **Project: <project-name>** > **Project
