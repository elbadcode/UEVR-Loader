# UEVR-Loader
simple python injector/loader for UEVR

I have a much more powerful loader in the works that just isnt ready for public release so for now throwing this out there as I've seen many people struggling with cases where this helps, particularly the usage of 3dmigoto alongside UEVR. This script will receive no future updates or maintenance as I will be focused on my other tool. If you need something more powerful than this, I am in the process of launching my [patreon](https://www.patreon.com/c/lobotomyx) and will soon have test builds available alongside many other goodies. (Have not yet posted as of 11/26/24)

This script requires that you can launch the game exe directly and does not have a listener mode. Again my wip tool can do both. For now if you cannot launch the exe directly you could try this brute force loader which is sometimes effective enough https://github.com/mirudo2/Custom-UEVR-Injector. I've also found success using extreme injector with thread hijacking in some games

# Regarding this script:

launches game as suspended process, automatically retrieves uevr dlls from your path with no hassle and manages starting and stopping the frontend

should suffice for most games without anticheat. for games with it there can be issues. 
if you need to get 3dmigoto into a uevr game just put it in uevr plugins folder with appropriately configured d3dx.ini and use this. UEVR is very good at loading DLLs but to load a graphics wrapper it needs to inject at startup

if starting from shortcut, bat, or cmd first arg is gamepath everything else is game args, otherwise use interactively

can handle double quotes so you can right click a game file and use copy as path without having to delete the quotes

for third party loaders you can try launching game normally and check the command line with systeminformer or similar and use that same command line here. Oftentimes that's all you need to bypass the launcher 

normally will inject openxr_loader but if you type "late" as an arg it will instead copy openxrloader into the gamedir after startup and you will have to manually click reinitialize runtime. This works and is needed for some games

compiled exe available and highly recommended if you want to make shortcuts  (otherwise you need some batch script shenanigans to pass args to python from a shortcut or I would have to write specific handlng), also includes python runtime environment

For developers and power users you may prefer to use the python script anyway so you can make adjustments

As always with compiled executables refer to [this helpful link if you think it could be a virus](https://github.com/elbadcode/NoItsNotaVirus)


# Example shortcut target 

```"N:\WinAppDev\Completed Utils\sussystart\uevrSS.exe" "F:\Wuthering Waves\Wuthering Waves Game\Client\Binaries\Win64\Client-Win64-Shipping.exe" "late"  "-d3d11"```
