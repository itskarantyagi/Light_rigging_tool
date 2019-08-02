# Light_rigging_tool

This is a lighting tool to create a light setup. User enters the details through a UI which is based on PyQt.


The tool provide 3 tpes of lighting rigs:
- 3 Point Lighting
- Fake GI
- IBL

About:

a. 3 Point Lighting : Using this tool will create 3 light setup - Key Light, Rim Light and Fill Light

b. Fake GI(Global Illumination) : Fake GI technique exploits the way LightWave antialiases and applies motion blur to a scene. Essentially, in order to antialias, LightWave just renders the scene several times with slight sub-pixel offsets to the positions of the rendered pixels. It then combines the results to give you the final render.

c. IBL : Image-based lighting (IBL) is a 3D rendering technique which involves capturing an omnidirectional representation of real-world light information as an image, typically using a specialized camera. This image is then projected onto a dome or sphere analogously to environment mapping, and this is used to simulate the lighting for the objects in the scene. This allows highly detailed real-world lighting to be used to light a scene, instead of trying to accurately model illumination using an existing rendering technique.
