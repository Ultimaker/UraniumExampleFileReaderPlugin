Example File Reader
===================

This is an example file reader plug-in for Uranium. Uranium is the underlying framework used in Ultimaker Cura.

File readers add support for opening certain types of files into the application. Their goal is to read the file from disk and create a scene node with the data that is represented by this file.

The plug-in first creates a mesh while reading the file. This mesh is put inside a scene node and the node is returned.

Packaging
---------

To create a plugin you can create a ZIP file from your complete plugin directory and rename it to use a .umplugin or .curaplugin extension.
