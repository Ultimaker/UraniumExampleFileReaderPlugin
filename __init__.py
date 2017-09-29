# Copyright (c) 2017 Ultimaker B.V.
# This example is released under the terms of the AGPLv3 or higher.

from . import ExampleFileReader

##  Defines additional metadata for the plug-in.
#
#   File reader type plug-ins must specify some additional metadata as to which
#   types of files they are able to read.
#   Some types of plug-ins require additional metadata, such as which file types
#   they are able to read or the name of the tool they define. In the case of
#   the "Extension" type plug-in, there is no additional metadata though.
def getMetaData():
    return {
        "mesh_reader": [ #A reader may be able to read multiple file types, so this is a list.
            {
                "extension": "txt",
                "description": "Example file type"
            }
        ]
    }

##  Lets Uranium know that this plug-in exists.
#
#   This is called when starting the application to find out which plug-ins
#   exist and what their types are. We need to return a dictionary mapping from
#   strings representing plug-in types (in this case "extension") to objects
#   that inherit from PluginObject.
#
#   \param app The application that the plug-in needs to register with.
def register(app):
    return {"mesh_reader": ExampleFileReader.ExampleFileReader()}
