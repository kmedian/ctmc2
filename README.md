[![Build Status](https://travis-ci.org/kmedian/ctmc2.svg?branch=master)](https://travis-ci.org/kmedian/ctmc2)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/kmedian/ctmc2/master?urlpath=lab)

# ctmc2
Continous Time Markov Chain (with automatic error correction)


## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `ctmc2` [git repo](http://github.com/kmedian/ctmc2) is available as [PyPi package](https://pypi.org/project/ctmc2)

```
pip install ctmc2
```


## Usage
Check the [examples](examples) folder for notebooks.


## Commands
* Check syntax: `flake8 --ignore=F401`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`


## Debugging
* Notebooks to profile python code are in the [profile](profile) folder


## Support
Please [open an issue](https://github.com/kmedian/ctmc2/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/kmedian/ctmc2/compare/).
