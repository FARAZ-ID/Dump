import os, platform

import requests

from os import system as cmd

os.system('git pull')
bit = platform.architecture()[0]

if bit == '64bit':

    from Dump import main

    main()

elif bit == '32bit':

    from Dump32 import main

    main()