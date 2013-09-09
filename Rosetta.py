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
        
        self.lang_support = []
        self.langDirList = []
    
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
        for (langID, langItem) in enumerate(langSupport):
            langSupport[langID][3] = lang_support.ProcessExtensionDescriptor(langItem[3])
        
        # Now store as part of the class file.
        self.langSupport = langSupport
        self.langDirList = langDirList

    def DetermineLanguage(self, filename = None, verbose = True):
        """
        This function determines the programming language from a
        particular file.
        """
        if filename is None:
            raise Exception("Filename needs to be specified.")
        if not os.path.exists(filename):
            raise IOError("File %s does not exist." % filename)
        if filename.find('.') == -1:
            raise IOError("File does not have an extension.")
        
        # At the moment, language determination is based on file extensions.
        extension = filename.rsplit('.')[1]
        matchingID = []

        for (langID, (language, version, description, supportedexts)) in enumerate(self.langSupport):
            if extension in supportedexts:
                matchingID.append(langID)
        if len(matchingID) == 1:
            if verbose:
                print("File %s appears to be written in %s.\n" % (filename, self.langSupport[matchingID[0]][0]))
            return matchingID[0]
        elif len(matchingID) == 0:
            raise Exception("Could not find a valid file descriptor for %s" % filename)
        else:
            raise NotImplementedError("Multiple languages found. Don't know what to do yet.")

if __name__ == "__main__":
    # This is run from a Terminal window
    ros = Rosetta()
    ros.CheckSupport()
    try:
        filename = sys.argv[1]
        langID1 = ros.DetermineLanguage(filename)
    except:
        sys.exit(-1)
    