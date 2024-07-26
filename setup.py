#! /usr/bin/python3

import src.utils as utils
import shutil

PACKAGES = "./packages.json"
REPO = "https://github.com/shubhamkode/.dotfiles.git"


def update_system():
    utils.sys_call(["sudo","apt","update"])
    utils.sys_call(["sudo","apt","upgrade" ,"-y"])


def install():
    packages = utils.read_json(PACKAGES)
    utils.install_snap_packages(packages["snap"])
    # utils.install_apt_packages(packages["apt"])


def stow_config():
    utils.sys_call(["stow",".","--adopt"])
    # utils.sys_call(["git","reset","--hard"])

def set_system():
    # set fish as default shell
    fish_dir = shutil.which("fish")
    assert fish_dir != None, "Fish not installed"
    utils.sys_call(["chsh" ,"-s", fish_dir])

    # set kitty as default terminal
    # kitty_dir = shutil.which("kitty")
    # assert kitty_dir != None, "Kitty not installed"





def main():
    step = 1
    utils.run(f"Step {step}: Updating System")(update_system)
    utils.run(f"Step {(step:=step+1)}: Installing Packages")(install)
    utils.run(f"Step {(step:=step+1)}: Stowing Configuration")(stow_config)
    utils.run(f"Step {(step:=step+1)}: Setting System")(set_system)
    print("Setup Completed\nRestart your session with i3.")




if __name__ == "__main__":
    main()