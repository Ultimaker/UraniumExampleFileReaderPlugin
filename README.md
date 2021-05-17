Example File Reader
===================

This is an example file reader plug-in for Uranium. Uranium is the underlying framework used in Ultimaker Cura and NinjaKittens.

File readers add support for opening certain types of files into the application. Their goal is to read the file from disk and create a scene node with the data that is represented by this file.

The plug-in first creates a mesh while reading the file. This mesh is put inside a scene node and the node is returned.

Packaging
---------

To package your plug-in, compress your plug-in folder in a .zip archive and rename that archive to get the `.plugin` extension. These .plugin files can be dropped into any Uranium application to be installed.
