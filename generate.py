import sys
import codecs

try:
    converted = "return{rom:["
    with open(sys.argv[1], "rb") as f:
        while (byte := f.read(1)):
            converted += "0x" + str(codecs.encode(byte, "hex"))[2:-1] + ","

    converted = converted[0:-1] + "]}"

    f = open("rom.spwn", "w")
    f.write(converted)
    f.close()
except IOError:
    print("File doesn't exist")