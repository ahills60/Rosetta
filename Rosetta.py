#!/usr/bin/env python

import sys, os, glob
import lang_support

class Rosetta:
    """
    Rosetta converts one programming language to another.
    """
    
    __version__ = '0.0.1'
    
    def __init__(self):
        """
        Creates an instance of the Rosetta class.
        """
        
        print("\nRosetta v%s by Andrew Hills <a.hills@sheffield.ac.uk>\n" % self.__version__)
    
    def CheckSupport(self, lang_dir = "languages", verbose = True):
        """
        The function CheckSupport determines what programming
        languages are supported by Rosetta.
        """
        if not os.path.exists(lang_dir):
            # Invalid language directory
            raise IOError("Language directory does not exist.")
        
        langDirList = glob.glob(lang_dir + os.path.sep + '*')
        # Filter list to directories only
        langDirList = [item for item in langDirList if os.path.isdir(item)]
        
        # Filter if language is valid
        langDirList = [item for item in langDirList if lang_support.ValidLanguage(item)]
        
        # Now list the languages and their descriptions
        langSupport = [lang_support.LanguageInfo(item) for item in langDirList]
        
        if verbose:
            print "Languages supported"
            print "-------------------\n"
            for (language, version, description, fileextensions) in langSupport:
                print("%s (%s)\t%s" % (language, version, description))
            print "\n"

if __name__ == "__main__":
    # This is run from a Terminal window
    ros = Rosetta()
    ros.CheckSupport()