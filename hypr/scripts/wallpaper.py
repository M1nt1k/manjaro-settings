#!/usr/bin/python
import os
import sys
import argparse

HOME = '/home/maximtimofeev'
path = f'{HOME}/.config/hypr/wallpapers/photos'
files = []

with os.scandir(path) as listOfEntries:  
    for entry in listOfEntries:
        if entry.is_file():
            files.append(entry.name)
        

def save(name):
    with open(f'{HOME}/.config/hypr/scripts/.actual', 'w') as wp:
        wp.write(name)

def load():
    with open(f'{HOME}/.config/hypr/scripts/.actual', 'r') as wp:
        name = wp.read().strip()
        return name

def next_wall():
    filename = load()
    if filename:
        index = files.index(filename)
        print(filename)
    else:
        index = 0

    index += 1
    if index >= len(files):
        index = 0

    os.system(f'swww img {path}/{files[index]}')
    save(files[index])

def prev_wall():
    filename = load()
    if filename:
        index = files.index(filename)
        print(filename)
    else:
        index = 0

    index -= 1
    if index < 0:
        index = len(files)-1

    os.system(f'swww img {path}/{files[index]}')
    save(files[index])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--inc', action='store_const', const=True, default=False)
    parser.add_argument('-p', '--dec', action='store_const', const=True, default=False)

    namespaces = parser.parse_args()
    print(files)
    print(namespaces)


    if namespaces.inc:
        next_wall()
    elif namespaces.dec:
        prev_wall()


if __name__ == "__main__":
    main()