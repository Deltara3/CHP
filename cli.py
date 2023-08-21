from sys import argv
from os import path, mkdir, listdir, remove
from codecs import encode

containing = path.dirname(path.realpath(__file__))

def build(location: str, name: str):
    try:
        converted = "return{data:["

        with open(location, "rb") as f:
            while (byte := f.read(1)):
                converted += "0x" + str(encode(byte, "hex"))[2:-1] + ","

        converted = converted[0:-1] + "]}"

        f = open(f"{containing}/built/{name}.8sp", "w")
        f.write(converted)
        f.close()

        print(f"info: converted '{path.basename(location)}' into '{name}.8sp")
    except FileNotFoundError:
        print(f"error: file '{path.basename(location)}' doesn't exist")
        exit(1)
    except PermissionError:
        print("error: cannot write built rom due to insufficent permissions")
        exit(1)

def switch(name: str):
    if path.isfile(f"{containing}/built/{name}.8sp"):
        try:
            f = open(f"{containing}/selection.spwn", "w")
            f.write(f"rom=import\"built/{name}.8sp\"" + ";return{rom:rom}")
            f.close()
            print(f"info: selected built rom '{name}'")
        except PermissionError:
            print("error: cannot write selection file due to insufficent permissions")
            exit(1)
    else:
        print(f"error: built rom '{name}' does not exist")
        exit(1)

def main():
    if not path.isdir(f"{containing}/built"):
        try:
            mkdir(f"{containing}/built")
        except PermissionError:
            print("error: cannot create built rom folder due to insufficent permissions")
            exit(1)

    match argv[1]:
        case "build":
            try:
                location = path.realpath(argv[2])
                name =  path.basename(location).split(".")[0]
                build(location, name)
                switch(name)
            except IndexError:
                print("error: expected file location")
                exit(1)
        case "switch":
            try:
                switch(argv[2])
            except IndexError:
                print("error: expected built rom name")
                exit(1)
        case "list":
            try:
                for rom in listdir(f"{containing}/built/"):
                    if rom.endswith(".8sp"):
                        formatted = rom.split(".")[0]
                        print(f"info: {formatted}")
            except FileNotFoundError:
                print("error: built rom folder does not exist")
                exit(1)
        case "delete":
            try:
                remove(f"{containing}/built/{argv[2]}.8sp")
                print(f"info: deleted built rom '{argv[2]}'")
            except FileNotFoundError:
                print(f"error: built rom '{argv[2]}' does not exist")
                exit(1)
            except IndexError:
                print("error: expected built rom name")
                exit(1)
        case "fix":
            print("\x1b[?25hinfo: cursor was made visible again")
        case other:
            print(f"error: invalid option '{other}'")
            exit(1)

main()