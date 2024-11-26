# UEVR-Loader
simple python injector/loader for UEVR

automatically retrieves uevr dlls from your path with no hassle and manages starting and stopping the frontend

should suffice for most games without anticheat. for games with it there can be issues. I have a much more powerful loader in the works that just isnt ready for public release so for now throwing this out there

if you need to get 3dmigoto into a uevr game just put it in uevr plugins folder and use this

if starting from shortcut, bat, or cmd first arg is gamepath everything else is game args, otherwise use interactively

can handle double quotes so you can right click a game file and use copy as path without havint to delete the quotes

normally will inject openxr_loader but if you type "late" as an arg it will instead copy openxrloader into the gamedir after startup and you will have to manually click reinitialize runtime. This works and is needed for some games

compiled exe available and highly recommended if you want to make shortcuts  (otherwise you need some batch script shenanigans to pass args to python from a shortcut or I would have to write specific handlng), also includes python runtime environment

As always with compiled executables refer to [this helpful link if you think it could be a virus](https://github.com/elbadcode/NoItsNotaVirus)
