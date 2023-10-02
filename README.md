# Sass Project Builder
The Sass Project Builder is a command line tool build in Python. It sets up a project with all folders for sass, an index.html, all necessary .scss-files and installs all npm packages. Depending on the requirements of your project you have the flexibility to choose (easy, advanced or expert) just a simple sass setup or 7-1-pattern.

## Installation

Download the Sass Project Builder files or install them via git clone:
'''
https://github.com/code-by-olof/sass-project-builder.git
'''

ou may have to install the following python libaries.

### Argsparse
```
python3 -m pip install argparse
```

## Usage

Show the help/usage
'''
python3 sass_builder.py -h
'''

### Set up a project with easy strcture
'''
python3 sass_builder.py -project projectname -pattern easy
'''
The following project structure will be created:

'''
--- projectname
    -- build
    -- public
    -- node_modules
    -- src
        -- sass
            - style.css
        - index.html
    - package-lock.json
    - package.json
'''

'''
- __projectname
  - build
  - public
  - node_modules
    - [cli.js](bin/cli.js)
  - [michal.png](michal.png)
  - [node\_modules](node_modules)
  - [npm\-debug.log](npm-debug.log)
  - [package.json](package.json)
  - [screen.png](screen.png)
  - __scripts__
    - [assert.js](scripts/assert.js)
    - [fancom.js](scripts/fancom.js)
    - [jshintrc.js](scripts/jshintrc.js)
    - [package\-json.js](scripts/package-json.js)
    - [precommit\-hook.js](scripts/precommit-hook.js)
    - [scripts.js](scripts/scripts.js)
    - [tests.js](scripts/tests.js)
  - __tests__
    - [michal\-tests.js](tests/michal-tests.js)
'''