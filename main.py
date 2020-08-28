import os
f = open("demofile.txt", "w")
i = 31
files = os.listdir(os.getcwd())

for file in files:
    if file.endswith(".ogg"):
        index_of_dot = file.index('.')
        filename = file[:index_of_dot]
        f.write("   \"" + filename + "\":{" + "\n")
        f.write("      \"category\":"
   "\"master\"," + "\n")
        f.write("      \"sounds\":[" + "\n")
        f.write("         \"" + filename + "\"" + "\n")
        f.write("      ]\r\n"
   "   }," + "\n")
