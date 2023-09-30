import sys
import os
import re
import argparse

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
            

achitecture_options = ["easy", "advanced", "expert"]

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