# coding = utf-8

import os
import shutil

path = 'E:/git/magua/second-day/problem2_files'

image_dir = path + '/image'
document_dir = path + '/document'

if not os.path.exists(image_dir):
    os.makedirs(image_dir)

if not os.path.exists(document_dir):
    os.makedirs(document_dir)

image_types = ['jpg', 'png', 'gif']
document_types = ['doc', 'docx', 'md', 'ppt']

for image_type in image_types:
    first_path = path + '/' + image_type
    image_files = os.listdir(first_path)
    for image_file in image_files:
        shutil.move(first_path + '/' + image_file, image_dir)
    os.removedirs(first_path)

for document_type in document_types:
    first_path = path + '/' + document_type
    document_files = os.listdir(first_path)
    for document_file in document_files:
        shutil.move(first_path + '/' + document_file, document_dir)
    os.removedirs(first_path)
