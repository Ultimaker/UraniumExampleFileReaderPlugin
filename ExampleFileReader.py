# Copyright (c) 2018 Ultimaker B.V.
# This example is released under the terms of the AGPLv3 or higher.

from UM.Application import Application #To pass to the parent constructor.
from UM.Mesh.MeshBuilder import MeshBuilder #To create a mesh to put in the scene.
from UM.Mesh.MeshReader import MeshReader #This is the plug-in object we need to implement if we want to create meshes. Otherwise extend from FileReader.
from UM.Math.Vector import Vector #Helper class required for MeshBuilder.
from UM.Scene.SceneNode import SceneNode #The result we must return when reading.

class ExampleFileReader(MeshReader):
    def __init__(self):
        super().__init__()
        self._supported_extensions = [".txt"] #Sorry, you also have to specify it here.

    ##  Read the specified file.
    #
    #   \return A scene node that represents what's in the file.
    def read(self, file_name):
        #Here you would typically open the file, read its contents, parse it, etc.
        #For this example we will just always create a cube and return that.

        builder = MeshBuilder() #To construct your own mesh, look at the methods provided by MeshBuilder.
        builder.addCube(10, 10, 10, Vector(0, 0, 0)) #Cube of 10 by 10 by 10.
        builder.calculateNormals()

        #Put the mesh inside a scene node.
        result_node = SceneNode()
        result_node.setMeshData(builder.build())
        result_node.setName(file_name) #Typically the file name that the mesh originated from is a good name for the node.

        return result_node