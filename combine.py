import os

outputFileName = "ALL.nanorc"
os.remove(outputFileName)

source = '.'
for root, dirs, filenames in os.walk(source):
    for file in filenames:
        if file.endswith(".nanorc"): 
            with open(file) as fp:
                for cnt, line in enumerate(fp):
                    output = open(outputFileName, "a")
                    output.write(line)
                    output.close()
                    
                output = open("ALL.nanorc", "a")
                output.write("# +EXTRALINT\n\n")
                output.close()

print("ALL.nanorc file created.")
