# Sass Project Builder
The Sass Project Builder is a command line tool build in Python. It sets up a project with all folders for sass, an index.html, all necessary .scss-files and installs all npm packages. Depending on the requirements of your project you have the flexibility to choose (easy, advanced or expert) just a simple sass setup or 7-1-pattern.

## Installation

Download the Sass Project Builder files or install them via git clone:
```
https://github.com/code-by-olof/sass-project-builder.git
```

ou may have to install the following python libaries.

### Argsparse
```
python3 -m pip install argparse
```

## Usage

Show the help/usage
```
python3 sass_builder.py -h
```

### Set up a project with easy strcture

```
python3 sass_builder.py -project projectname -pattern easy
```
The following project structure will be created:

```
- PROJECTNAME
  - build
  - public
  - node_modules
    - ...
  - src
      - index.html
      - sass
         - style.scss
  - package-lock.json
  - package.json
```

### Set up a project with avancded strcture

The advancded structure includes only selected folder and files from the 7-1-architecture pattern.
You can adjust the structure in the Python file to your projects needs.

```
python3 sass_builder.py -project projectname -pattern advanced
```
The following project structure (based on the default settings) will be created:

```
- PROJECTNAME
  - build
  - public
  - node_modules
    - ...
  - src
      - index.html
      - sass
         - abstracts
            - _mixsins.scss
            - _variables.scss
         - base
            - _reset.scss
            - _typography.scss
         - components
            - _buttons.scss 
         - layout
            - _footer.scss 
            - _forms.scss 
            - _grid.scss 
            - _header.scss 
            - _footer.scss 
            - _navigation.scss
            - _sidebar.scss                                        
         - style.scss
  - package-lock.json
  - package.json
```


### Set up a project with expert strcture

The expert structure includes all folders and files of the 7-1-architecture pattern.
You also can adjust the names of the files and folders in the Python file.

```
python3 sass_builder.py -project projectname -pattern expert
```
The following project structure (based on the default settings) will be created:


```
- PROJECTNAME
  - build
  - public
  - node_modules
    - ...
  - src
      - index.html
      - sass
         - abstracts
            - _mixsins.scss
            - _variables.scss
            - _functions.scss
            - _placeholders.scss
         - base
            - _reset.scss
            - _typography.scss
         - components
            - _buttons.scss 
            - _carousel.scss 
            - _cover.scss 
            - _dropdon.scss 
         - layout
            - _footer.scss 
            - _forms.scss 
            - _grid.scss 
            - _header.scss 
            - _footer.scss 
            - _navigation.scss
            - _sidebar.scss  
         - pages
            - _home.scss
            - _contact.scss
         - themes
            - _light.scss
            - _dark.scss 
            - _admin.scss
         - themes
            - _bootstrap.scss
            - _jquery-ui.scss                                                                             
         - style.scss
  - package-lock.json
  - package.json
```


### Start coding in your project

After creating the project with easy, advanced or expert pattern, navigate into your direcectory and start sass.

```
cd projectname
```

```
npm start
```