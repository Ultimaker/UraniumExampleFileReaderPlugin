Example File Reader
===================

This is an example file reader plug-in for Uranium.

File readers add support for opening certain types of files into the application. Their goal is to read the file from disk and create a scene node with the data that is represented by this file.

The plug-in first creates a mesh while reading the file. This mesh is put inside a scene node and the node is returned.

Packaging
---------

To package your plug-in, use the packaging script in Uranium: https://github.com/Ultimaker/Uranium/blob/master/create_plugin.py

Try the following command:

    python3 /path/to/Uranium/create_plugin.py plugin_location /path/to/UraniumExampleExtensionPlugin

That should produce a .plugin file that can be added to any application based on Uranium.