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

## Adjust the default settings

In the Python file (sass_builder.py) there is an array of objects called sass_architecture.

```
sass_architecture = [ 
    { 
        "folder": "abstracts",
        "files" : [
            [ "variables", True, True, "var" ],
            [ "functions", False, True, "func" ],
            [ "mixins", True, True, "mix" ],
            [ "placeholders", False, True, "plc" ]            
        ] 
    },
    { 
        "folder": "base",
        "files" : [
            [ "reset", True, False ],
            [ "typography", True, False ]         
        ] 
    },
    { 
        "folder": "components",
        "files" : [
            [ "buttons", True, False ],
            [ "carousel", False, False ],
            [ "cover", False, False ],
            [ "dropdown", False, False ]          
        ] 
    },
    { 
        "folder": "layout",
        "files" : [
            [ "navigation", True, False ],
            [ "grid", True, False ],
            [ "header", True, False ],
            [ "footer", True, False ],
            [ "sidebar", True, False ],
            [ "forms", True, False ]          
        ] 
    },
    { 
        "folder": "pages",
        "files" : [
            [ "home", False, False],
            [ "contact", False, False ]         
        ] 
    },
    { 
        "folder": "themes",
        "files" : [
            [ "light", False, False ],
            [ "dark", False, False ],
            [ "admin", False, False ]          
        ] 
    },
    { 
        "folder": "vendors",
        "files" : [
            [ "bootstrap", False, False ],
            [ "jquery-ui", False, False ]         
        ] 
    }    
]
```

Let's take a closer look:
```
[ "variables", True, True, "var" ]
```
1. Value: name of the .scss-file
2. Value: True/False --> File is/is not included in Advanced Pattern
3. Value: True/False -> File should be imported (@use) in other files. Should only be set true in files such as variables, functions...
4. Value: namespace - optional - can be provided if it is a file that needs to be imported. 3. value musst be set to true then.

If you change the names settings (2 - 4), it effects the usage for projects with advanced pattern. The expert pattern will always include all foldern and files.
You can change the names of the files and folders and of course, you can add or remove files and folders.


## Package.json

The Python file has an array with the name package_json.
```
package_json = [
     '{',
     '\t"name": "project",',
     '\t"version": "0.1.0",',
     '\t"description": "created by Sass Project Builder",',
     '\t"main": "public/index.html",',
     '\t"author": "code-by-olof",',
     '\t"scripts": {',
     '\t\t"build:sass": "sass  --no-source-map src/sass:public/",',
     '\t\t"copy:html": "copyfiles -u 1 ./src/*.html public",',
     '\t\t"copy": "npm-run-all --parallel copy:*",',
     '\t\t"watch:html": "onchange \'src/*.html\' -- npm run copy:html",',
     '\t\t"watch:sass": "sass  --no-source-map --watch src/sass:public/",',
     '\t\t"watch": "npm-run-all --parallel watch:*",',
     '\t\t"serve": "browser-sync start --server public --files public",',
     '\t\t"start": "npm-run-all copy --parallel watch serve",',
     '\t\t"build": "npm-run-all copy:html build:*",',
     '\t\t"postbuild": "postcss public/css/*.css -u autoprefixer cssnano -r --no-map"',
     '\t},',
     '\t"dependencies": {',
     '\t\t"autoprefixer": "^10.4.16",',
     '\t\t"browser-sync": "^2.29.3",',
     '\t\t"copyfiles": "^2.4.1",',
     '\t\t"cssnano": "^6.0.1",',
     '\t\t"npm-run-all": "^4.1.5",',
     '\t\t"onchange": "^7.1.0",',
     '\t\t"postcss-cli": "^10.1.0",',
     '\t\t"sass": "^1.68.0"',
     '\t}',
     '}'
]
```

All the dependencies are currentyl (October 2023) up to date.
After installing all npm packages there should be no error.
