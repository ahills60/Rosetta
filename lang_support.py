"""
This script provides language support functionality
"""

import os

lang_desc_fn = "lang.desc"

def ValidLanguage(lang_path = None):
    """
    Checks for the presence of a language descriptor file.
    """
    if lang_path is None:
        raise Exception("Invalid language specified.")
    descriptorFile = lang_path + os.path.sep + lang_desc_fn
    return os.path.exists(descriptorFile)

def LanguageInfo(lang_path = None):
    """
    Returns information on the programming language based on
    the language descriptor file.
    
    Output: language name, version, description, file exts
    """
    descriptorFile = lang_path + os.path.sep + lang_desc_fn
    if not os.path.exists(descriptorFile):
        raise IOError("Language descriptor file not found.")
    
    # Create variable storage
    outputList = ["", "", "", ""]
    
    # Now read descriptor file.
    fin = open(descriptorFile, 'r')
    
    idx = -1
    
    for line in fin:
        # Iteratively go through this file
        if line.find(':') == -1:
            # Possibly a continuation of the previous field
            if idx == -1:
                # No, it wasn't
                continue
            else:
                outputList[ent] += " " + line.strip()
        name, content = line.split(":", 1)
        name = name.strip().lower()
        content = content.strip()
        
        if name == 'language':
            idx = 0
        elif name == 'version':
            idx = 1
        elif name == 'description':
            idx = 2
        elif name == 'fileextensions':
            idx = 3
            
        outputList[idx] = content
    fin.close()
    return outputList