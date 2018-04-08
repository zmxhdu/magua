# coding = utf-8

import os
import filecmp


def get_all_files(path, dirs):
    all_files = []
    for dir in dirs:
        cur_path = path + '/' + dir
        files = os.listdir(cur_path)
        for file in files:
            all_files.append(cur_path + '/' + file)
    return all_files


def cmp_files(x, y):
    if filecmp.cmp(x, y):
        os.remove(y)
        print("路径\"" + y + "\"下的文件是重复文件，已删除")


if __name__ == '__main__':
    problem3_path = './problem3_files'
    dirs = ['pic1', 'pic2']

    all_files = get_all_files(problem3_path, dirs)

    for x in all_files:
        for y in all_files:
            if x!=y and os.path.exists(x) and os.path.exists(y):
                cmp_files(x, y)