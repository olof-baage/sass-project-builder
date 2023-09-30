import sys
import os
import argparse

class Project:
    def __init___(self):
        self.projectname = ""

    @property
    def projectname(self):
        return self._projectname

    @projectname.setter
    def projectname(self, projectname):
        self._fprojectname = projectname

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

    if len(sys.argv) == 1:
        parser.print_help()
    
    print("Projectname: ", args.project)
    print("Pattern: ", args.pattern)
    print("Dir: ", args.dir)

if __name__ == "__main__":
    main()