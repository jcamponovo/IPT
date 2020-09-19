import os
g = open("trust.sh","w")
g.write("#!/bin/bash\n")
liste = os.listdir()
for f in liste:
    if f[-6:] == ".ipynb":
        os.popen("jupyter trust {}".format(f))
        print("jupyter trust {}".format(f))
        g.write("jupyter trust {}\n".format(f))
g.close()
