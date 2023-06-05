from pathlib import Path
import sys
import subprocess

sys.path.append("../dependencies/dev_scripts")
from build_ark import build_patch_ark
from build_dx_settings_ark import build_dxsl_ark
from check_git_updated import check_git_updated

# get the current working directory
cwd = Path(__file__).parent
root_dir = Path(__file__).parents[1] # root directory of the repo

cmd_xenia = "_xenia\\xenia_canary.exe _build\\xbox\\default.xex"

tbrbdx_res = True
if check_git_updated(repo_url="https://github.com/hmxmilohax/beatles-rock-band-deluxe", repo_root_path=root_dir):
    if not root_dir.joinpath("_build/xbox/gen/patch_xbox_0.ark").is_file():
        print("The Beatles Rock Band Deluxe ark not found, building it now...")
        tbrbdx_res = build_patch_ark(True)
else:
    print("Local repo out of date, pulling and building an updated The Beatles Rock Band Deluxe ark now...")
    tbrbdx_res = build_patch_ark(True)
    
if tbrbdx_res:
    print("Ready to run The Beatles Rock Band Deluxe in Xenia.")
    subprocess.run(cmd_xenia, shell=True, cwd="..")
# if tbrbdx_res:
#     print("Ready to run The Beatles Rock Band Deluxe in Xenia.")
#     subprocess.run(cmd_xenia, shell=True, cwd="..")