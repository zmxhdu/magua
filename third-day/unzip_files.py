# coding = utf-8

import os
import shutil
import time


image_path = './image'
output_path = './output'
zip_count = 0

while True:
    files = os.listdir(image_path)
    files_count = len(files)
    if files_count >= 5:
        zip_count += 1
        zip_name = output_path + '/' + 'archive' + str(zip_count)
        shutil.make_archive(zip_name, 'zip', image_path)
        for f in files:
            os.remove(image_path + '/' + f)
    time.sleep(1)
