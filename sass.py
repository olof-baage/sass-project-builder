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
            else:
                sys.exit("\n😱 Directory does not exist or can't be created.\nIf you want to create your project in a subfolder or in a folder outside of this, make sure, to provide a valid name.\nA folder name should only contain the chars A-Z, a-z, 0-9 and ._- and has to end with /.\ne.g. -dir ../afolder/asubfolder/ OR just-a-subfolder/\n")
        else:
             self._project_dir = "./"    


    def create_main_project_folders(self):
        os.chdir(self.project_dir)
        os.mkdir(self.project_name)
        os.chdir(self.project_name + "/")
        for folder in main_folders:
            os.mkdir(folder + "/")

    def write_package_json(self):
        with open("package.json", "a") as file:
            for entry in package_json:
                file.write(f"{entry}\n")

    
    def install_depencies(self):
        subprocess.check_call('npm install', shell=True)
            

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
     '\t\t"build:sass": "sass  --no-source-map src/sass:public/css",',
     '\t\t"copy:html": "copyfiles -u 1 ./src/*.html public",',
     '\t\t"copy": "npm-run-all --parallel copy:*",',
     '\t\t"watch:html": "onchange \'src/*.html\' -- npm run copy:html",',
     '\t\t"watch:sass": "sass  --no-source-map --watch src/sass:public/css",',
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
            sassproject.install_depencies()


def validate_projectname(projectname):
    if re.search(r"[a-zA-Z0-9-_\.]$", projectname):
        return True


def validate_path(path):
	if re.search(r"^(\.\./|\./)?([a-z-A-Z_\.0-9]*(/){1})*$", path):
		if os.path.isdir("./" + path) == False:
			os.mkdir("./" + path)
		return True
	return False


if __name__ == "__main__":
    main()