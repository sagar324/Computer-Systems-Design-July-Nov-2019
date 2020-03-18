s = input()
index=0
with open(s + ".vm", 'r') as file1:
    filecontent = file1.readlines()
i = len(filecontent)
file2 = open(s + ".asm", 'w')
for j in range(i):
    for k in range(len(filecontent[j])):
        if (filecontent[j][k] == "/"):
            filecontent[j] = filecontent[j][:k]
            filecontent[j] += "\n"
            break

i = len(filecontent)
num = -2
for j in range(i):
    filecontent[j] = filecontent[j].split()
for j in range(i):
    #print(filecontent)
    if(len(filecontent[j])!=0):
        if ((filecontent[j][0]) == "push"):
            ind = filecontent[j][2]
            if (filecontent[j][1] == "constant"):
                file2.write("@" + ind + "\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif (filecontent[j][1] == "argument"):
                file2.write("@ARG\nD=M\n@" + ind + "\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif (filecontent[j][1] == "temp"):
                file2.write("@5\nD=A\n@" + ind + "\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif (filecontent[j][1] == "that"):
                file2.write("@THAT\nD=M\n@" + ind + "\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif (filecontent[j][1] == "this"):
                file2.write("@THIS\nD=M\n@" + ind + "\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif (filecontent[j][1] == "local"):
                file2.write("@LCL\nD=M\n@" + ind + "\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif (filecontent[j][1] == "pointer"):
                file2.write("@3\nD=A\n@" + ind + "\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif (filecontent[j][1] == "static"):
                file2.write("@"+s+ ind + "\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

        elif ((filecontent[j][0]) == "pop"):
            ind = filecontent[j][2]
            if (filecontent[j][1] == "constant"):
                print("error")

            elif (filecontent[j][1] == "argument"):
                file2.write("@ARG\nD=M\n@" + ind + "\nD=A+D\n@R13\nM=D\n@SP\nA=M\nA=A-1\nD=M\n@R13\nA=M\nM=D\n@SP\nM=M-1\n")
            elif (filecontent[j][1] == "temp"):
                file2.write("@5\nD=A\n@" + ind + "\nD=A+D\n@R13\nM=D\n@SP\nA=M\nA=A-1\nD=M\n@R13\nA=M\nM=D\n@SP\nM=M-1\n")
            elif (filecontent[j][1] == "that"):
                file2.write(
                    "@THAT\nD=M\n@" + ind + "\nD=A+D\n@R13\nM=D\n@SP\nA=M\nA=A-1\nD=M\n@R13\nA=M\nM=D\n@SP\nM=M-1\n")
            elif (filecontent[j][1] == "this"):
                file2.write(
                    "@THIS\nD=M\n@" + ind + "\nD=A+D\n@R13\nM=D\n@SP\nA=M\nA=A-1\nD=M\n@R13\nA=M\nM=D\n@SP\nM=M-1\n")
            elif (filecontent[j][1] == "local"):
                file2.write("@LCL\nD=M\n@" + ind + "\nD=A+D\n@R13\nM=D\n@SP\nA=M\nA=A-1\nD=M\n@R13\nA=M\nM=D\n@SP\nM=M-1\n")
            elif (filecontent[j][1] == "pointer"):
                file2.write("@3\nD=A\n@" + ind + "\nD=A+D\n@R13\nM=D\n@SP\nA=M\nA=A-1\nD=M\n@R13\nA=M\nM=D\n@SP\nM=M-1\n")
            elif (filecontent[j][1] == "static"):
                file2.write("@SP\nA=M\nA=A-1\nD=M\n@"+s+ ind + "\nM=D\n@SP\nM=M-1\n")
        elif ((filecontent[j][0]) == "add"):
            file2.write("@SP\nA=M\nA=A-1\nD=M\nA=A-1\nM=D+M\n@SP\nM=M-1\n")
        elif ((filecontent[j][0]) == "sub"):
            file2.write("@SP\nA=M\nA=A-1\nD=M\nA=A-1\nM=M-D\n@SP\nM=M-1\n")
        elif ((filecontent[j][0]) == "eq"):
            num += 2
            file2.write("@SP\nA=M\nA=A-1\nD=M\nA=A-1\nD=M-D\n@ALABEL_" + str(num) + "\nD;JEQ\nD=0\n@ALABEL_" + str(
                num + 1) + "\n0;JMP\n(ALABEL_" + str(num) + ")\nD=-1\n(ALABEL_" + str(
                num + 1) + ")\n@SP\nM=M-1\nA=M\nA=A-1\nM=D\n")
        elif ((filecontent[j][0]) == "lt"):
            num += 2
            file2.write("@SP\nA=M\nA=A-1\nD=M\nA=A-1\nD=M-D\n@ALABEL_" + str(num) + "\nD;JLT\nD=0\n@ALABEL_" + str(
                num + 1) + "\n0;JMP\n(ALABEL_" + str(num) + ")\nD=-1\n(ALABEL_" + str(
                num + 1) + ")\n@SP\nM=M-1\nA=M\nA=A-1\nM=D\n")
        elif ((filecontent[j][0]) == "gt"):
            num += 2
            file2.write("@SP\nA=M\nA=A-1\nD=M\nA=A-1\nD=M-D\n@ALABEL_" + str(num) + "\nD;JGT\nD=0\n@ALABEL_" + str(
                num + 1) + "\n0;JMP\n(ALABEL_" + str(num) + ")\nD=-1\n(ALABEL_" + str(
                num + 1) + ")\n@SP\nM=M-1\nA=M\nA=A-1\nM=D\n")
        elif ((filecontent[j][0]) == "and"):
            file2.write("@SP\nA=M\nA=A-1\nD=M\nA=A-1\nM=M&D\n@SP\nM=M-1\n")
        elif ((filecontent[j][0]) == "or"):
            file2.write("@SP\nA=M\nA=A-1\nD=M\nA=A-1\nM=M|D\n@SP\nM=M-1\n")
        elif ((filecontent[j][0]) == "not"):
            file2.write("@SP\nA=M\nA=A-1\nM=!M\n")
        elif ((filecontent[j][0]) == "neg"):
            file2.write("@SP\nA=M\nA=A-1\nM=-M\n")
        elif((filecontent[j][0])=="label"):
            k = filecontent[j][1]
            file2.write("("+k+")\n")
        elif((filecontent[j][0])=="goto"):
            k=filecontent[j][1]
            file2.write("@"+k+"\n0;JMP\n")
        elif((filecontent[j][0])=="if-goto"):
            k = filecontent[j][1]
            file2.write("@SP\nAM=M-1\nD=M\n@" + k + "\nD;JNE\n")
        elif((filecontent[j][0])=="call"):
            k = filecontent[j][1]
            g= filecontent[j][2]
            file2.write("@"+s+k+"_return_"+str(index)+"\nD=A\n@SP\nAM=M+1\nA=A-1\nM=D\n@LCL\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n@ARG\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n@THIS\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n@THAT\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n@SP\nD=M\n@5\nD=D-A\n@"+g+"\nD=D-A\n@ARG\nM=D\n@"+k+"\n0;JMP\n"+"("+s+k+"_return_"+str(index)+")\n")
            index=index+1
        elif((filecontent[j][0])=="function"):
            k=filecontent[j][1]
            g = filecontent[j][2]
            file2.write("("+k+")\n"+"@SP\nD=M\n@LCL\nM=D\n@"+g+"\nD=A\n("+k+"_loop)\n@"+k+"_end\nD;JEQ\n@SP\nAM=M+1\nA=A-1\nM=0\nD=D-1\n@"+k+"_loop\n0;JMP\n("+k+"_end)\n")
        elif((filecontent[j][0])=="return"):
            file2.write("@LCL\nD=M\n@R14\nM=D\n@5\nD=D-A\nA=D\nD=M\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D\nD=A+1\n@SP\nM=D\n@R14\nAM=M-1\nD=M\n@THAT\nM=D\n@R14\nAM=M-1\nD=M\n@THIS\nM=D\n@R14\nAM=M-1\nD=M\n@ARG\nM=D\n@R14\nAM=M-1\nD=M\n@LCL\nM=D\n@R13\nA=M\n0;JMP\n")
                                  
file2.close()
