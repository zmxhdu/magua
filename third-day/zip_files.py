# coding = utf-8

import os
import shutil


def scan_zip():
    files = os.lisdir()
    for f in files:
        if f.endswith('.zip'):
            return f

def unzip_it(f):
    folder_name = f.split('.')[0]
    target_path = './' + folder_name
    os.makedirs(target_path)
    shutil.unpack_archive(f, target_path)


def delete_zip(f):
    os.remove(f)

while True:
    zip_file = scan_zip()
    if zip_file:
        unzip_it(zip_file)
        delete_zip(zip_file)
