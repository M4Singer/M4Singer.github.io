import glob
import os
import json
from tqdm import tqdm

wav_fns = sorted(
    glob.glob(f'CSV/*/*')
)

map_tab = {'声乐1号女#暖暖#11': '1', '声乐1号女#贝加尔湖畔#18': '2' , '女高音5号#青藏高原#8': '3', '女高音5号#春晓#5': '4',
           '声乐男声2号#理想三旬#17': '5', '声乐男声2号#十年#10': '6', '男低音3#听海#37': '7', '男低音3#听海#46': '8'}

for wav_fn in wav_fns:
    item_name = os.path.basename(wav_fn)[:-4]
    type = os.path.basename(wav_fn)[-4:]
    dir_name = os.path.dirname(wav_fn)
    for key in map_tab.keys():
        if key in item_name:
            new_path = dir_name + '/' + map_tab[key] + type
            os.rename(wav_fn, new_path)
            break

    #print(dir_name)
    #print(item_name)
    #print(type)