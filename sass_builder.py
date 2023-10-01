import sys
import os
import re
import argparse
import subprocess

class Project:
    def __init___(self):
        self.project_name = ""
        self.project_type = ""
        self.project_dir = "./"

    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        self._project_name = project_name

    @property
    def project_type(self):
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        self._project_type = project_type
    
    @property
    def project_dir(self):
        return self._project_dir

    @project_dir.setter
    def project_dir(self, project_dir):
        self._project_dir = project_dir        

    
    def save_settings(self, name, pattern, dir=""):
        self._project_name = name
        self._project_type = pattern
        if dir != None:
            if validate_path(dir):
                self._project_dir = dir
            elif validate_path == False:
                sys.exit("\n😱 Project directory couldn't be created!\n\nIf there is already a folder with the same name, rename or delete that folder or chose another dir-name.\n\nIf you want to create your project in a subfolder or in a folder outside of this, make sure, to provide a valid name.\nA folder name should only contain the chars A-Z, a-z, 0-9 and ._- and has to end with /.\ne.g. -dir ../afolder/asubfolder/ OR just-a-subfolder/\n")
        else:
             self._project_dir = "./"    


    def create_main_project_folders(self):
        os.chdir(self.project_dir)
        try:
            os.mkdir(self.project_name)
        except FileExistsError:
            sys.exit("\n😱 Project directory couldn't be created!\n\nIf there is already a folder with the same name, rename or delete that folder or chose another dir-name.\n\nIf you want to create your project in a subfolder or in a folder outside of this, make sure, to provide a valid name.\nA folder name should only contain the chars A-Z, a-z, 0-9 and ._- and has to end with /.\ne.g. -dir ../afolder/asubfolder/ OR just-a-subfolder/\n")            
        os.chdir(self.project_name + "/")        
        for folder in main_folders:
            os.mkdir(folder + "/")
        os.mkdir("src/sass/")
        fscss = open("src/sass/style.scss", "w")
        fscss.close()
        with open("src/index.html", "a") as file:
            for entry in htmlindex:
                file.write(f"{entry}\n")
        print("🤩 main folders successfully created.\n")

    def write_package_json(self):
        with open("./package.json", "a") as file:
            for entry in package_json:
                file.write(f"{entry}\n")
        print("🤩 package.json successfully created.\n")

    
    def install_depencies(self):
        subprocess.check_call('npm install', shell=True)

    def build_sass_architecture(self):
        for item in sass_architecture:       
            files = item['files'] 
            if self.project_type == "advanced":
                if has_folder_files(files):
                    write_folders(files, item, self.project_type)
            if self.project_type == "expert":
                write_folders(files, item, self.project_type)   


achitecture_options = ["easy", "advanced", "expert"]
main_folders = ["src", "public", "build"]
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

htmlindex = [
    '<!DOCTYPE html>',
    '<html lang="en">',
    '<head>',
    '\t<meta charset="UTF-8">',
    '\t<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '\t<title>made by Sass Project Builder 😇 </title>',
    '\t<link rel="stylesheet" href="style.css">',
    '</head>',
    '<body>',
    '\t<h1>Hej från Olof 👋</h1>',
    '\t<p>Vad kul att du använder Sass Project Builder! 🤩</p>'
    '\t</body>'
    '\t</html>'
]

'''
Sass Architecture
[ 
    "_variables.scss",  --> filename
      True/False,       --> file is included in ADVANCED pattern
      True/False        --> file needs to be includes in other files. important for vars (colors, typography...), mixins
      "var"             --> namespace (optional)
]
- Won't be used for projects with pattern EASY
- Includes all folders with files (set to true) with at least one file set to true with pattern ADVANCED 
- Includes all folders and its files with pattern EXPERT 
'''
sass_architecture = [ 
    { 
        "folder": "abstracts",
        "files" : [
            [ "_variables.scss", True, True, "var" ],
            [ "_functions.scss", False, True, "func" ],
            [ "_mixins.scss", True, True, "mix" ],
            [ "_placeholders.scss", False, True, "plc" ]            
        ] 
    },
    { 
        "folder": "base",
        "files" : [
            [ "_reset.scss", True, True ],
            [ "_typography.scss", True, False ]         
        ] 
    },
    { 
        "folder": "components",
        "files" : [
            [ "_buttons.scss", True, False ],
            [ "_carousel.scss", False, False ],
            [ "_cover.scss", False, False ],
            [ "_dropdown.scss", False, False ]          
        ] 
    },
    { 
        "folder": "layout",
        "files" : [
            [ "_navigation.scss", True, False ],
            [ "_grid.scss", True, False ],
            [ "_header.scss", True, False ],
            [ "_footer.scss", True, False ],
            [ "_sidebar.scss", True, False ],
            [ "_forms.scss", True, False ]          
        ] 
    },
    { 
        "folder": "pages",
        "files" : [
            [ "_home.scss", False, False],
            [ "_contact.scss", False, False ]         
        ] 
    },
    { 
        "folder": "themes",
        "files" : [
            [ "_theme.scss", False, False ],
            [ "_admin.scss", False, False ]         
        ] 
    },
    { 
        "folder": "vendors",
        "files" : [
            [ "_bootstrap.scss", False, False ],
            [ "_jquery-ui.scss", False, False ]         
        ] 
    }    
]

def main():
    '''
    Settings for CLI parser
    '''
    parser = argparse.ArgumentParser(prog='SassProjectBuilder', description='Sass project Builder')
    parser.usage = "\n\nSTART A PROJECT:\nsass -project projectname -pattern easy | advanced | expert"
    parser.add_argument("-project", help="projectname e.g. LinkedIn-Clone")
    parser.add_argument("-dir", help="path to a directory")
    parser.add_argument("-pattern", help="your architecture pattern for sass", choices=achitecture_options)
    args = parser.parse_args()

    sassproject = Project()

    if len(sys.argv) == 1:
        parser.print_help()       

    if args.project != None and args.pattern != None:
        if validate_projectname(args.project):
            sassproject.save_settings(args.project, args.pattern, args.dir)
            sassproject.create_main_project_folders()
            sassproject.write_package_json()
            #sassproject.install_depencies()
            sassproject.build_sass_architecture()


def validate_projectname(projectname):
    if re.search(r"^[a-zA-Z0-9-_\.]*$", projectname):
        return True
    else:
        return False


def validate_path(path):
    if re.search(r"^(((\.\/){1}(\.\.\/)*)|(\.\/){1}|(\.\.\/)*)[a-z-A-Z-_\.0-9]*(\/){1}$", path):
        return True
    else:
        return False


def has_folder_files(files):
    count = 0
    for file in files:
        if(file[1]):
            count += 1
    if count >= 1:
        return True
    return False   


def write_file_dependencies(file):
    for folder in sass_architecture:
        all_files = folder['files']
        for single_file in all_files:
            if single_file[2]:
                if len(single_file) == 4:                                  
                    file.write("@use '../" + folder['folder'] + "/" + single_file[0] +"' as " + single_file[3] + ";\n") 
                else:
                    file.write("@use '../" + folder['folder'] + "/" + single_file[0] + ";\n") 


def write_folders(files, item, pattern):
    os.mkdir("src/sass/" + item['folder'] + "/")     
    for file in files:
        if pattern == "advanced":
            if file[1]:
                fscss = open("src/sass/" + item['folder'] + "/" + file[0], "w")
                write_file_dependencies(fscss)
                fscss.close()
        elif pattern == "expert": 
            fscss = open("src/sass/" + item['folder'] + "/" + file[0], "w")
            write_file_dependencies(fscss)
            fscss.close()            


if __name__ == "__main__":
    main()