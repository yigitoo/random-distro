import webbrowser
import random
from info import (
    list_of_distros,
    list_of_eol_distros
)

class DistroChooser:
    global distro_list, eol_distro_list
    distro_list = list_of_distros
    eol_distro_list = list_of_eol_distros
            
    @staticmethod
    def choose() -> str:
        are_you_want_eol = input('Do you want EOL Distros: ')

        if "yes" in are_you_want_eol:
            distro_list.append(eol_distro_list)

        return distro_list[random.randint(0, len(distro_list) - 1)]



webbrowser.open(DistroChooser.choose(), new = 2)
