__author__ = 'Eshin Kunishima'
__license__ = 'MIT'

import argparse
import os
import re
import time


class Demover:
    def __init__(self):
        pass

    @staticmethod
    def move(source, destination, threshold=60):
        now = time.time()

        for dem in filter(lambda name: os.path.isfile(name) and re.match('.+\.dem$', name), os.listdir(source)):
            src = os.path.join(source, dem)
            dest = os.path.join(destination, dem)

            if now - os.path.getmtime(src) >= threshold:
                os.rename(src, dest)


def main():
    parser = argparse.ArgumentParser(description='The demo(.dem) file mover for CS:S and CS:GO written in Python')
    parser.add_argument('src', type=str, help='Source directory')
    parser.add_argument('dst', type=str, help='Destination directory')

    arguments = parser.parse_args()

    Demover.move(arguments.src, arguments.dst)


if __name__ == '__main__':
    main()
