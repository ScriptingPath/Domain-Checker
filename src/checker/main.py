import grequests

from datetime import datetime
from os import makedirs

domains = []


def make_folders():
    try:
        makedirs("settings")
    except FileExistsError:
        pass

    with open("settings/domains.txt", "a"):
        pass


def load_domains():
    global domains

    try:
        with open("settings/domains.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                domains.append(line)
    except FileNotFoundError:
        path = input("Enter path to file with domains: ")

        with open(path, "r") as file:
            for line in file.readlines():
                domains.append(line)


def create_result_folder():
    now = datetime.now()

    try:
        makedirs(
            f"results/result_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}")
    except FileExistsError:
        makedirs(
            f"results/result_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}")


def check():
    pass


def main():
    make_folders()
    load_domains()
    create_result_folder()
    check()


if __name__ == '__main__':
    main()
