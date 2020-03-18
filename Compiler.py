n = int(input("no of files"))

nextprosflag = 1


def comment(k):
    global flag
    global jackfile
    for b in range(len(jackfile[k])):
        if jackfile[k][b] == '*' and jackfile[k][b + 1] == '/':
            jackfile[k] = jackfile[k][b + 2:]
            flag = 0
            checkjack(k)
            return
    return


def issymb(l) -> type(int):
    if l == '{':
        return 1
    elif l == '}':
        return 1
    elif l == '(':
        return 1
    elif l == ')':
        return 1
    elif l == '[':
        return 1
    elif l == ']':
        return 1
    elif l == '.':
        return 1
    elif l == ',':
        return 1
    elif l == ';':
        return 1
    elif l == '+':
        return 1
    elif l == '-':
        return 1
    elif l == '*':
        return 1
    elif l == '/':
        return 1
    elif l == '&':
        return 1
    elif l == '|':
        return 1
    elif l == '<':
        return 1
    elif l == '>':
        return 1
    elif l == '=':
        return 1
    elif l == '~':
        return 1
    elif l == ' ':
        return 1
    else:
        return 0


def keyword(q):
    global jackt
    jackt = jackt + len(q)
    filepars.write("<keyword> " + q + " </keyword>\n")
    checkjack(jackj)
    return


def symbol(w):
    filepars.write("<symbol> " + w + " </symbol>\n")
    global jackt,jackj
    jackt = jackt + 1
    if jackj==i-1:
        return
    checkjack(jackj)
    return


def identifier():
    global jackt
    z = jackt + 1
    global jackfile
    while not issymb(jackfile[jackj][z]):
        z = z + 1
    e = jackfile[jackj][jackt:z]
    filepars.write("<identifier> " + e + " </identifier>\n")
    jackt = z
    checkjack(jackj)
    return


def integerconstant():
    global jackt
    z = jackt + 1
    global jackfile
    while not (issymb(jackfile[jackj][z])):
        z = z + 1
    r = jackfile[jackj][jackt:z]
    filepars.write("<integerConstant> " + r + " </integerConstant>\n")
    jackt = z
    checkjack(jackj)
    return


def stringconstant():
    global jackt
    z = jackt + 1
    global jackfile
    while jackfile[jackj][z] != '"':
        z = z + 1
    y = jackfile[jackj][jackt + 1:z]
    filepars.write("<stringConstant> " + y + "</stringConstant>\n")
    jackt = z + 1
    checkjack(jackj)
    return


def checkjack(k):
    global jackt
    global flag
    global jackfile
    if jackfile[k][jackt] == "A":
        identifier()
        return
    elif jackfile[k][jackt] == "B":
        identifier()
        return
    elif jackfile[k][jackt] == "C":
        identifier()
        return
    elif jackfile[k][jackt] == "D":
        identifier()
        return
    elif jackfile[k][jackt] == "E":
        identifier()
        return
    elif jackfile[k][jackt] == "F":
        identifier()
        return
    elif jackfile[k][jackt] == "G":
        identifier()
        return
    elif jackfile[k][jackt] == "H":
        identifier()
        return
    elif jackfile[k][jackt] == "I":
        identifier()
        return
    elif jackfile[k][jackt] == "J":
        identifier()
        return
    elif jackfile[k][jackt] == "K":
        identifier()
        return
    elif jackfile[k][jackt] == "L":
        identifier()
        return
    elif jackfile[k][jackt] == "M":
        identifier()
        return
    elif jackfile[k][jackt] == "N":
        identifier()
        return
    elif jackfile[k][jackt] == "O":
        identifier()
        return
    elif jackfile[k][jackt] == "P":
        identifier()
        return
    elif jackfile[k][jackt] == "Q":
        identifier()
        return
    elif jackfile[k][jackt] == "R":
        identifier()
        return
    elif jackfile[k][jackt] == "S":
        identifier()
        return
    elif jackfile[k][jackt] == "T":
        identifier()
        return
    elif jackfile[k][jackt] == "U":
        identifier()
        return
    elif jackfile[k][jackt] == "V":
        identifier()
        return
    elif jackfile[k][jackt] == "W":
        identifier()
        return
    elif jackfile[k][jackt] == "X":
        identifier()
        return
    elif jackfile[k][jackt] == "Y":
        identifier()
        return
    elif jackfile[k][jackt] == "Z":
        identifier()
        return
    elif jackfile[k][jackt] == "a":
        identifier()
        return
    elif jackfile[k][jackt] == "b":
        if jackfile[k][jackt:jackt + 7] == "boolean" and issymb(jackfile[k][jackt + 7]):
            keyword("boolean")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "c":
        if jackfile[k][jackt:jackt + 5] == "class" and issymb(jackfile[k][jackt + 5]):
            keyword("class")
        elif jackfile[k][jackt:jackt + 4] == "char" and issymb(jackfile[k][jackt + 4]):
            keyword("char")
        elif jackfile[k][jackt:jackt + 11] == "constructor" and issymb(jackfile[k][jackt + 11]):
            keyword("constructor")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "d":
        if jackfile[k][jackt:jackt + 2] == "do" and issymb(jackfile[k][jackt + 2]):
            keyword("do")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "e":
        if jackfile[k][jackt:jackt + 4] == "else" and issymb(jackfile[k][jackt + 4]):
            keyword("else")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "f":
        if jackfile[k][jackt:jackt + 8] == "function" and issymb(jackfile[k][jackt + 8]):
            keyword("function")
        elif jackfile[k][jackt:jackt + 5] == "false" and issymb(jackfile[k][jackt + 5]):
            keyword("false")
        elif jackfile[k][jackt:jackt + 5] == "field" and issymb(jackfile[k][jackt + 5]):
            keyword("field")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "g":
        identifier()
        return
    elif jackfile[k][jackt] == "h":
        identifier()
        return
    elif jackfile[k][jackt] == "i":
        if jackfile[k][jackt:jackt + 3] == "int" and issymb(jackfile[k][jackt + 3]):
            keyword("int")
        elif jackfile[k][jackt:jackt + 2] == "if" and issymb(jackfile[k][jackt + 2]):
            keyword("if")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "j":
        identifier()
        return
    elif jackfile[k][jackt] == "k":
        identifier()
        return
    elif jackfile[k][jackt] == "l":
        if jackfile[k][jackt:jackt + 3] == "let" and issymb(jackfile[k][jackt + 3]):
            keyword("let")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "m":
        if jackfile[k][jackt:jackt + 6] == "method" and issymb(jackfile[k][jackt + 6]):
            keyword("method")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "n":
        if jackfile[k][jackt:jackt + 4] == "null" and issymb(jackfile[k][jackt + 4]):
            keyword("null")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "o":
        identifier()
        return
    elif jackfile[k][jackt] == "p":
        identifier()
        return
    elif jackfile[k][jackt] == "q":
        identifier()
        return
    elif jackfile[k][jackt] == "r":
        if jackfile[k][jackt:jackt + 6] == "return" and issymb(jackfile[k][jackt + 6]):
            keyword("return")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "s":
        if jackfile[k][jackt:jackt + 6] == "static" and issymb(jackfile[k][jackt + 6]):
            keyword("static")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "t":
        if jackfile[k][jackt:jackt + 4] == "this" and issymb(jackfile[k][jackt + 4]):
            keyword("this")
        elif jackfile[k][jackt:jackt + 4] == "true" and issymb(jackfile[k][jackt + 4]):
            keyword("true")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "u":
        identifier()
        return
    elif jackfile[k][jackt] == "v":
        if jackfile[k][jackt:jackt + 4] == "void" and issymb(jackfile[k][jackt + 4]):
            keyword("void")
        elif jackfile[k][jackt:jackt + 3] == "var" and issymb(jackfile[k][jackt + 3]):
            keyword("var")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "w":
        if jackfile[k][jackt:jackt + 5] == "while" and issymb(jackfile[k][jackt + 5]):
            keyword("while")
        else:
            identifier()
        return
    elif jackfile[k][jackt] == "x":
        identifier()
        return
    elif jackfile[k][jackt] == "y":
        identifier()
        return
    elif jackfile[k][jackt] == "z":
        identifier()
        return
    elif jackfile[k][jackt] == "{":
        symbol('{')
        return
    elif jackfile[k][jackt] == "}":
        symbol('}')
        return
    elif jackfile[k][jackt] == "(":
        symbol('(')
        return
    elif jackfile[k][jackt] == ")":
        symbol(')')
        return
    elif jackfile[k][jackt] == "[":
        symbol('[')
        return
    elif jackfile[k][jackt] == "]":
        symbol(']')
        return
    elif jackfile[k][jackt] == ".":
        symbol('.')
        return
    elif jackfile[k][jackt] == ",":
        symbol(',')
        return
    elif jackfile[k][jackt] == ";":
        symbol(';')
        return
    elif jackfile[k][jackt] == "+":
        symbol('+')
        return
    elif jackfile[k][jackt] == "-":
        symbol('-')
        return
    elif jackfile[k][jackt] == "*":
        symbol('*')
        return
    elif jackfile[k][jackt] == "/":
        if jackfile[k][jackt + 1] == "/":
            # print("no\n")
            return
        elif jackfile[k][jackt + 1] == "*":
            # print("sa\n")
            flag = 1
            comment(k)
            return
        else:
            symbol('/')
        return
    elif jackfile[k][jackt] == "&":
        symbol('&')
        return
    elif jackfile[k][jackt] == "|":
        symbol('|')
        return
    elif jackfile[k][jackt] == "<":
        symbol('<')
        return
    elif jackfile[k][jackt] == ">":
        symbol('>')
        return
    elif jackfile[k][jackt] == "=":
        symbol('=')
        return
    elif jackfile[k][jackt] == "~":
        symbol('~')
        return
    elif jackfile[k][jackt] == " ":
        jackt = jackt + 1
        # print("dd\n")
        checkjack(k)
        return
    elif jackfile[k][jackt] == '"':
        stringconstant()
        return
    elif jackfile[k][jackt] == "1":
        integerconstant()
        return
    elif jackfile[k][jackt] == "2":
        integerconstant()
        return
    elif jackfile[k][jackt] == "3":
        integerconstant()
        return
    elif jackfile[k][jackt] == "4":
        integerconstant()
        return
    elif jackfile[k][jackt] == "5":
        integerconstant()
        return
    elif jackfile[k][jackt] == "6":
        integerconstant()
        return
    elif jackfile[k][jackt] == "7":
        integerconstant()
        return
    elif jackfile[k][jackt] == "8":
        integerconstant()
        return
    elif jackfile[k][jackt] == "9":
        integerconstant()
        return
    elif jackfile[k][jackt] == "0":
        integerconstant()
        return
    elif jackfile[k][jackt] == "\t":
        jackt = jackt + 1
        checkjack(k)
    else:
        return





#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################


# n = input()
parsv = 0
space = 0

def checkparse(k) -> type(int):
    if filecontent[k][1] == 'k':
        t = filecontent[k][10:13]
        if t == "cla":
            return 0
        if t == "con":
            return 5
        if t == "fun":
            return 6
        if t == "met":
            return 7
        if t == "fie":
            return 8
        if t == "sta":
            return 9
        if t == "var":
            return 10
        if t == "int":
            return 11
        if t == "cha":
            return 12
        if t == "boo":
            return 13
        if t == "voi":
            return 14
        if t == "tru":
            return 15
        if t == "fal":
            return 16
        if t == "nul":
            return 17
        if t == "thi":
            return 18
        if t == "let":
            return 19
        if t == "do ":
            return 20
        if t == "if ":
            return 21
        if t == "els":
            return 22
        if t == "whi":
            return 23
        if t == "ret":
            return 24
        else:
            print("error")
            nextprosflag = 0
            return 25
    if filecontent[k][1] == 's' and filecontent[k][2] == 'y':
        t = filecontent[k][9]
        if t == '{':
            return 26
        elif t == '}':
            return 27
        elif t == '(':
            return 28
        elif t == ')':
            return 29
        elif t == '[':
            return 30
        elif t == ']':
            return 31
        elif t == '.':
            return 32
        elif t == ',':
            return 33
        elif t == ';':
            return 34
        elif t == '+':
            return 35
        elif t == '-':                                              
            return 36
        elif t == '*':
            return 37
        elif t == '/':
            return 38
        elif t == '&':
            return 39
        elif t == '|':
            return 40
        elif t == '<':
            return 41
        elif t == '>':
            return 42
        elif t == '=':
            return 43
        elif t == '~':
            return 44
    if filecontent[k][1] == 's' and filecontent[k][2] == 't':
        return 2
    if filecontent[k][1] == 'i' and filecontent[k][2] == 'd':
        return 3
    if filecontent[k][1] == 'i' and filecontent[k][2] == 'n':
        t = 9
        flag = 0
        while filecontent[k][t] != '<' and filecontent[k][t + 1] != '/':
            for a in range(10):
                if filecontent[k][t] == str(a):
                    flag = 1
            t = t + 1
        if flag == 0:
            print("error")
            nextprosflag = 0
            return
        return 4


def compvardec():
    global space
    kfile.write(" " * space + "<varDec>\n")
    global parsv
    space += 2
    if checkparse(parsv) == 10:
        kfile.write(" " * space + filecontent[parsv])
    else:
        print("error : expected var\n")
        nextprosflag = 0
        return
    parsv = parsv + 1
    if checkparse(parsv) == 11 or checkparse(parsv) == 12 or checkparse(parsv) == 13 or checkparse(parsv) == 3:
        kfile.write(" " * space + filecontent[parsv])
    else:
        print("error : expected type\n")
        nextprosflag = 0
        return
    parsv = parsv + 1
    if checkparse(parsv) == 3:
        kfile.write(" " * space + filecontent[parsv])
    else:
        print("error : expected varName\n")
        nextprosflag = 0
        return
    parsv = parsv + 1
    while checkparse(parsv) != 34:
        if checkparse(parsv) == 33:
            kfile.write(" " * space + filecontent[parsv])
        else:
            print("error : expected ',' ")
            nextprosflag = 0
            return
        if checkparse(parsv + 1) == 3:
            kfile.write(" " * space + filecontent[parsv + 1])
        else:
            print("error : expected var name after','")
            nextprosflag = 0
            return
        parsv = parsv + 2
    kfile.write(" " * space + filecontent[parsv])
    parsv = parsv + 1
    space -= 2
    kfile.write(" " * space + "</varDec>\n")


def compclassvardec():
    global space
    kfile.write(" " * space + "<classVarDec>\n")
    global parsv
    space += 2
    if checkparse(parsv) == 8 or checkparse(parsv) == 9:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected static or filed")
        nextprosflag = 0
        return
    if checkparse(parsv) == 11 or checkparse(parsv) == 12 or checkparse(parsv) == 13 or checkparse(parsv) == 3:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected type")
        nextprosflag = 0
        return
    if checkparse(parsv) == 3:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected var name")
        nextprosflag = 0
        return
    while checkparse(parsv) != 34:
        if checkparse(parsv) == 33:
            kfile.write(" " * space + filecontent[parsv])
        else:
            print("error : expected ',' ")
            nextprosflag = 0
            return
        if checkparse(parsv + 1) == 3:
            kfile.write(" " * space + filecontent[parsv + 1])
            parsv = parsv + 2
        else:
            print("error : expected var name ")
            nextprosflag = 0
            return
    kfile.write(" " * space + filecontent[parsv])
    parsv = parsv + 1
    space -= 2
    kfile.write(" " * space + "</classVarDec>\n")


def compsubroutinebody():
    global space
    kfile.write(" " * space + "<subroutineBody>\n")
    global parsv
    space += 2
    if checkparse(parsv) == 26:
        kfile.write(" " * space + filecontent[parsv])
    else:
        print("error : expected '{' \n")
        nextprosflag = 0
        return
    parsv = parsv + 1
    while checkparse(parsv) == 10:
        compvardec()
    if checkparse(parsv) == 19 or checkparse(parsv) == 20 or checkparse(parsv) == 21 or checkparse(
            parsv) == 23 or checkparse(parsv) == 24:
        while checkparse(parsv) == 19 or checkparse(parsv) == 20 or checkparse(parsv) == 21 or checkparse(
                parsv) == 23 or checkparse(parsv) == 24:
            compstatements()
    else:
        print("error : expected statemet after {")
        nextprosflag = 0
        return
    if checkparse(parsv) == 27:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected '}' \n")
        nextprosflag = 0
        return
    space -= 2
    kfile.write(" " * space + "</subroutineBody>\n")


def compsubroutinecall():
    global space
    global parsv
    # kfile.write(" " * space + "<subroutineCall>\n")
    if checkparse(parsv) == 3 and checkparse(parsv + 1) == 28:
        kfile.write(" " * space + filecontent[parsv])
        kfile.write(" " * space + filecontent[parsv + 1])
        parsv = parsv + 2
        compexpressionlist()
        if checkparse(parsv) == 29:
            kfile.write(" " * space + filecontent[parsv])
            parsv = parsv + 1
        else:
            print("error : expected ')' ")
            nextprosflag = 0
            return
    elif checkparse(parsv) == 3 and checkparse(parsv + 1) == 32:
        kfile.write(" " * space + filecontent[parsv])
        kfile.write(" " * space + filecontent[parsv + 1])
        parsv = parsv + 2
        if checkparse(parsv) == 3:
            kfile.write(" " * space + filecontent[parsv])
            parsv = parsv + 1
        else:
            print("error : expected subroutineName ")
            nextprosflag = 0
            return
        if checkparse(parsv) == 28:
            kfile.write(" " * space + filecontent[parsv])
            parsv = parsv + 1
        else:
            print("error : expected '(' ")
            nextprosflag = 0
            return
        compexpressionlist()
        if checkparse(parsv) == 29:
            kfile.write(" " * space + filecontent[parsv])
            parsv = parsv + 1
        else:
            print("error : expected ')' ")
            nextprosflag = 0
            return
    else:
        print("error : expected '.' or '(' ")
        nextprosflag = 0
        return
    # kfile.write(" "*space+"</subroutineCall>\n")


def compsubroutinedec():
    global space
    global parsv
    kfile.write(" " * space + "<subroutineDec>\n")
    space += 2
    kfile.write(" " * space + filecontent[parsv])
    parsv += 1
    if checkparse(parsv) == 12 or checkparse(parsv) == 13 or checkparse(parsv) == 14 or checkparse(
            parsv) == 3 or checkparse(parsv) == 11:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected void or type")
        nextprosflag = 0
        return
    if checkparse(parsv) == 3:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected subroutineName ")
        nextprosflag = 0
        return
    if checkparse(parsv) == 28:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected '(' ")
        nextprosflag = 0
        return
    compparameterlist()
    if checkparse(parsv) == 29:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected ')' ")
        nextprosflag = 0
        return
    if checkparse(parsv) == 26:
        compsubroutinebody()
    else:
        print("error : expected subroutineBody")
        nextprosflag = 0
        return
    space -= 2
    kfile.write(" " * space + "</subroutineDec>\n")


def compparameterlist():
    global space
    global parsv
    kfile.write(" " * space + "<parameterList>\n")
    space += 2
    if checkparse(parsv) == 11 or checkparse(parsv) == 12 or checkparse(parsv) == 13 or checkparse(parsv) == 3:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
        if checkparse(parsv) == 3:
            kfile.write(" " * space + filecontent[parsv])
            parsv += 1
        else:
            print("error : expected varName")
            nextprosflag = 0
            return
        if checkparse(parsv) == 33:
            while checkparse(parsv) == 33:
                kfile.write(" " * space + filecontent[parsv])
                parsv += 1
                if checkparse(parsv) == 11 or checkparse(parsv) == 12 or checkparse(parsv) == 13 or checkparse(
                        parsv) == 3:
                    kfile.write(" " * space + filecontent[parsv])
                    parsv += 1
                if checkparse(parsv) == 3:
                    kfile.write(" " * space + filecontent[parsv])
                    parsv += 1
    space -= 2
    kfile.write(" " * space + "</parameterList>\n")


def compterm():
    global parsv
    global space
    kfile.write(" " * space + "<term>\n")
    space += 2
    if checkparse(parsv) == 4:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    elif checkparse(parsv) == 2:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    elif checkparse(parsv) == 15:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    elif checkparse(parsv) == 16:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    elif checkparse(parsv) == 17:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    elif checkparse(parsv) == 18:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    elif checkparse(parsv) == 3 and checkparse(parsv + 1) != 30 and checkparse(parsv + 1) != 28 and checkparse(
            parsv + 1) != 32:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    elif checkparse(parsv) == 3 and checkparse(parsv + 1) == 30:
        kfile.write(" " * space + filecontent[parsv])
        kfile.write(" " * space + filecontent[parsv + 1])
        parsv = parsv + 2
        compexpression()
        if checkparse(parsv) == 31:
            kfile.write(" " * space + filecontent[parsv])
            parsv = parsv + 1
        else:
            print("error : expected ']' ")
            nextprosflag = 0
            return
    elif checkparse(parsv) == 3 and checkparse(parsv + 1) == 28:
        compsubroutinecall()
    elif checkparse(parsv) == 3 and checkparse(parsv + 1) == 32:
        compsubroutinecall()
    elif checkparse(parsv) == 28:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
        compexpression()
        if checkparse(parsv) == 29:
            kfile.write(" " * space + filecontent[parsv])
            parsv = parsv + 1
        else:
            print("error : expected ')' ")
            nextprosflag = 0
            return
    elif checkparse(parsv) == 36 or checkparse(parsv) == 44:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
        compterm()
    else:
        print("error : not a term")
        nextprosflag = 0
        return
    space -= 2
    kfile.write(" " * space + "</term>\n")


def compstatements():
    global space
    global parsv
    kfile.write(" " * space + "<statements>\n")
    space += 2
    if checkparse(parsv) == 19 or checkparse(parsv) == 20 or checkparse(parsv) == 23 or checkparse(
            parsv) == 24 or checkparse(parsv) == 21:
        while checkparse(parsv) == 19 or checkparse(parsv) == 20 or checkparse(parsv) == 23 or checkparse(
                parsv) == 24 or checkparse(parsv) == 21:
            compstatement()
            # if checkparse(parsv) == 19:
            #     completstatement()
            # if checkparse(parsv) == 20:
            #     compdostatement()
            # if checkparse(parsv) == 21:
            #     compifstatement()
            # if checkparse(parsv) == 23:
            #     compwhilestatement()
            # if checkparse(parsv) == 24:
            #     compreturnstatement()
            # parsv += 1
    space -= 2
    kfile.write(" " * space + "</statements>\n")


def compstatement():
    global space
    global parsv
    if checkparse(parsv) == 19:
        completstatement()
    if checkparse(parsv) == 20:
        compdostatement()
    if checkparse(parsv) == 21:
        compifstatement()
    if checkparse(parsv) == 23:
        compwhilestatement()
    if checkparse(parsv) == 24:
        compreturnstatement()


def compreturnstatement():
    global space
    kfile.write(" " * space + "<returnStatement>\n")
    global parsv
    space += 2
    if checkparse(parsv) == 24:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected return ")
        nextprosflag = 0
        return

    if checkparse(parsv) == 2 or checkparse(parsv) == 4 or checkparse(parsv) == 15 or checkparse(
            parsv) == 16 or checkparse(parsv) == 17 or checkparse(parsv) == 18 or checkparse(parsv) == 3 or checkparse(
            parsv) == 28 or checkparse(parsv) == 44 or checkparse(parsv) == 36:
        compexpression()
    if checkparse(parsv) == 34:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected ';' after return statement")
        nextprosflag = 0
        return
    space -= 2

    kfile.write(" " * space + "</returnStatement>\n")


def compdostatement():
    global space
    kfile.write(" " * space + "<doStatement>\n")
    global parsv
    space += 2
    if checkparse(parsv) == 20:
        kfile.write(" " * space + filecontent[parsv])
    else:
        print("error")
        nextprosflag = 0
        return
    parsv = parsv + 1
    if checkparse(parsv) == 3:
        compsubroutinecall()
    else:
        print("error")
        nextprosflag = 0
        return
    if checkparse(parsv) == 34:
        kfile.write(" " * space + filecontent[parsv])
    else:
        print("error : expected ';' after do statement")
        nextprosflag = 0
        return
    parsv = parsv + 1
    space -= 2
    kfile.write(" " * space + "</doStatement>\n")


def compwhilestatement():
    global space
    kfile.write(" " * space + "<whileStatement>\n")
    space += 2
    global parsv
    if checkparse(parsv) == 23:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error")
        nextprosflag = 0
        return
    if checkparse(parsv) == 28:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected '(' in while after 'while' ")
        nextprosflag = 0
        return
    if checkparse(parsv) == 2 or checkparse(parsv) == 4 or checkparse(parsv) == 15 or checkparse(
            parsv) == 16 or checkparse(parsv) == 17 or checkparse(parsv) == 18 or checkparse(parsv) == 3 or checkparse(
            parsv) == 28 or checkparse(parsv) == 44 or checkparse(parsv) == 36:
        compexpression()
    else:
        print("error : expected expression in while after '('")
        nextprosflag = 0
        return
    if checkparse(parsv) == 29:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected ')' in while after expression")
        nextprosflag = 0
        return
    if checkparse(parsv) == 26:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected '{' in while after ')'")
        nextprosflag = 0
        return
    while checkparse(parsv) == 19 or checkparse(parsv) == 20 or checkparse(parsv) == 21 or checkparse(
            parsv) == 23 or checkparse(parsv) == 24:
        compstatements()
    if checkparse(parsv) == 27:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected '}' after while statement ")
        nextprosflag = 0
        return
    space -= 2
    kfile.write(" " * space + "</whileStatement>\n")


def completstatement():
    global space
    global parsv
    kfile.write(" " * space + "<letStatement>\n")
    space += 2
    kfile.write(" " * space + filecontent[parsv])
    parsv += 1
    if checkparse(parsv) == 3:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    if checkparse(parsv) == 30:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
        compexpression()
        if checkparse(parsv) == 31:
            kfile.write(" " * space + filecontent[parsv])
            parsv = parsv + 1
        else:
            print("error : expected ']'")
            nextprosflag = 0
            return
    if checkparse(parsv) == 43:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected '=' in let ")
        nextprosflag = 0
        return
    compexpression()
    if checkparse(parsv) == 34:
        kfile.write(" " * space + filecontent[parsv])
        parsv = parsv + 1
    else:
        print("error : expected ';' in let after expression")
        nextprosflag = 0
        return
    space -= 2
    kfile.write(" " * space + "</letStatement>\n")


def compifstatement():
    global space
    global parsv
    kfile.write(" " * space + "<ifStatement>\n")
    space += 2
    kfile.write(" " * space + filecontent[parsv])
    parsv += 1
    if checkparse(parsv) == 28:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected '(' in if statement after if")
        nextprosflag = 0
        return
    compexpression()
    if checkparse(parsv) == 29:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected ')' in if after expression")
        nextprosflag = 0
        return
    if checkparse(parsv) == 26:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected '{' after in if ')' ")
        nextprosflag = 0
        return
    compstatements()
    if checkparse(parsv) == 27:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected '}' in if after statements ")
        nextprosflag = 0
        return
    if checkparse(parsv) == 22:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
        if checkparse(parsv) == 26:
            kfile.write(" " * space + filecontent[parsv])
            parsv += 1
        else:
            print("error : expected '{' ")
            nextprosflag = 0
            return
        compstatements()
        if checkparse(parsv) == 27:
            kfile.write(" " * space + filecontent[parsv])
            parsv += 1
        else:
            print("error : expected '}' ")
            nextprosflag = 0
            return
    space -= 2
    kfile.write(" " * space + "</ifStatement>\n")


def compexpressionlist():
    global space
    global parsv
    kfile.write(" " * space + "<expressionList>\n")
    space += 2
    if checkparse(parsv) == 4 or checkparse(parsv) == 2 or checkparse(parsv) == 15 or checkparse(
            parsv) == 16 or checkparse(parsv) == 17 or checkparse(parsv) == 18 or checkparse(
            parsv) == 3 or checkparse(parsv) == 28 or checkparse(parsv) == 36 or checkparse(parsv) == 44:
        compexpression()
        if checkparse(parsv) == 33:
            while checkparse(parsv) == 33:
                kfile.write(" " * space + filecontent[parsv])
                parsv += 1
                if checkparse(parsv) == 4 or checkparse(parsv) == 2 or checkparse(parsv) == 15 or checkparse(
                        parsv) == 16 or checkparse(parsv) == 17 or checkparse(
                        parsv) == 18 or checkparse(parsv) == 3 or checkparse(parsv) == 28 or checkparse(
                    parsv) == 36 or checkparse(parsv) == 44:
                    compexpression()
    space -= 2
    kfile.write(" " * space + "</expressionList>\n")


def compexpression():
    global space
    global parsv
    kfile.write(" " * space + "<expression>\n")
    space += 2
    if checkparse(parsv) == 4 or checkparse(parsv) == 2 or checkparse(parsv) == 15 or checkparse(
            parsv) == 16 or checkparse(parsv) == 17 or checkparse(parsv) == 18 or checkparse(
            parsv) == 3 or checkparse(parsv) == 28 or checkparse(parsv) == 36 or checkparse(parsv) == 44:
        compterm()
    if checkparse(parsv) == 35 or checkparse(parsv) == 36 or checkparse(parsv) == 37 or checkparse(
            parsv) == 38 or checkparse(parsv) == 39 or checkparse(
            parsv) == 40 or checkparse(parsv) == 41 or checkparse(parsv) == 42 or checkparse(parsv) == 43:
        while checkparse(parsv) == 35 or checkparse(parsv) == 36 or checkparse(parsv) == 37 or checkparse(
                parsv) == 38 or checkparse(parsv) == 39 or checkparse(
                parsv) == 40 or checkparse(parsv) == 41 or checkparse(parsv) == 42 or checkparse(parsv) == 43:
            kfile.write(" " * space + filecontent[parsv])
            parsv += 1
            compterm()
    space -= 2
    kfile.write(" " * space + "</expression>\n")


def compclass():
    global parsv
    global space
    kfile.write(" " * space + "<class>\n")
    space += 2
    kfile.write(" " * space + filecontent[parsv])
    parsv += 1
    if checkparse(parsv) == 3:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected className ")
        nextprosflag = 0
        return
    if checkparse(parsv) == 26:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected '{' ")
        nextprosflag = 0
        return
    if checkparse(parsv) == 8 or checkparse(parsv) == 9 or checkparse(parsv) == 5 or checkparse(
            parsv) == 6 or checkparse(parsv) == 7:
        while checkparse(parsv) == 8 or checkparse(parsv) == 9 or checkparse(parsv) == 5 or checkparse(
                parsv) == 6 or checkparse(parsv) == 7:
            if checkparse(parsv) == 8 or checkparse(parsv) == 9:
                compclassvardec()
            elif checkparse(parsv) == 5 or checkparse(parsv) == 6 or checkparse(parsv) == 7:
                compsubroutinedec()
    else:
        print("error : expected clasvarDec or subroutineDec ")
        nextprosflag = 0
        return
    if checkparse(parsv) == 27:
        kfile.write(" " * space + filecontent[parsv])
        parsv += 1
    else:
        print("error : expected '}' ")
        nextprosflag = 0
        return
    space -= 2
    kfile.write(" " * space + "</class>\n")


def parse():
    global s
    global parsv
    parsv += 1
    print ("parsev = " + str(parsv))
    print("f="+filecontent[parsv])
    if checkparse(parsv) == 0:
        compclass()
    else:
        print("error : class not found")
        nextprosflag = 0
        return







#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################

# n = input()



class variable():
    def __init__(self, namein, typein, kindin, noin):
        self.name = namein
        self.type = typein
        self.kind = kindin
        self.no = noin

def main():
    global vmv
    # print(filep[vmv]+str(vmv))
    if check(vmv) == 101:
        print("here")
        compileclass()
    for x in subroutine_symbol_table:
        print(x.name)
    for x in class_symbol_table:
        print(x.name)


def extract(k) -> type(str):
    e = ""
    x = 0
    while filep[k][x] != '>':
        x += 1
    x += 1
    if filep[k][x] == ' ':
        x += 1
    r = x
    while filep[k][x] != '<':
        x += 1
    if filep[k][x - 1] == ' ':
        e = filep[k][r:x - 1]
        return e
    e = filep[k][x]
    return e


def check(k) -> type(int):

    if "<keyword>" in filep[k]:
        i = 0
        while filep[k][i] != ">":
            i += 1
        i += 1
        if filep[k][i] == " ":
            i += 1
        t = filep[k][i:i+3]
        if t == "cla":
            return 0
        if t == "con":
            return 5
        if t == "fun":
            return 6
        if t == "met":
            return 7
        if t == "fie":
            return 8
        if t == "sta":
            return 9
        if t == "var":
            return 10
        if t == "int":
            return 11
        if t == "cha":
            return 12
        if t == "boo":
            return 13
        if t == "voi":
            return 14
        if t == "tru":
            return 15
        if t == "fal":
            return 16
        if t == "nul":
            print("NULLLLLL")
            return 17
        if t == "thi":
            return 18
        if t == "let":
            return 19
        if t == "do ":
            return 20
        if t == "if ":
            return 21
        if t == "els":
            return 22
        if t == "whi":
            return 23
        if t == "ret":
            return 24
        else:
            print("error00")
            return 25
    if "<symbol>" in filep[k]:
        i = 0
        while filep[k][i] != ">":
            i += 1
        i += 1
        if filep[k][i] == " ":
            i += 1
        t = filep[k][i]
        if t == '{':
            return 26
        elif t == '}':
            return 27
        elif t == '(':
            return 28
        elif t == ')':
            return 29
        elif t == '[':
            return 30
        elif t == ']':
            return 31
        elif t == '.':
            return 32
        elif t == ',':
            return 33
        elif t == ';':
            return 34
        elif t == '+':
            return 35
        elif t == '-':
            return 36
        elif t == '*':
            return 37
        elif t == '/':
            return 38
        elif t == '&':
            return 39
        elif t == '|':
            return 40
        elif t == '<':
            return 41
        elif t == '>':
            return 42
        elif t == '=':
            return 43
        elif t == '~':
            return 44
    if "<stringConstant>" in filep[k]:
        return 2
    if "<identifier>" in filep[k]:
        return 3
    if "<integerConstant>" in filep[k]:
        return 4
        t = 9
        flag = 0
        while filep[k][t] != '<' and filep[k][t + 1] != '/':
            for a in range(10):
                if filep[k][t] == str(a):
                    flag = 1
            t = t + 1
        if flag == 0:
            print("error23")
            return
        return 4
    if "<class>" in filep[k]:
        return 101
    if "</class>" in filep[k]:
        return 102
    if "<classVarDec>" in filep[k]:
        return 103
    if "</classVarDec>" in filep[k]:
        return 104
    if "<subroutineDec>" in filep[k]:
        return 105
    if "</subroutineDec>" in filep[k]:
        return 106
    if "<parameterList>" in filep[k]:
        return 107
    if "</parameterList>" in filep[k]:
        return 108
    if "<subroutineBody>" in filep[k]:
        return 109
    if "</subroutineBody>" in filep[k]:
        return 110
    if "<varDec>" in filep[k]:
        return 111
    if "</varDec>" in filep[k]:
        return 112
    if "<statements>" in filep[k]:
        return 113
    if "</statements>" in filep[k]:
        return 114
    if "<letStatement>" in filep[k]:
        return 115
    if "</letStatement>" in filep[k]:
        return 116
    if "<ifStatement>" in filep[k]:
        return 117
    if "</ifStatement>" in filep[k]:
        return 118
    if "<whileStatement>" in filep[k]:
        return 119
    if "</whileStatement>" in filep[k]:
        return 120
    if "<doStatement>" in filep[k]:
        return 121
    if "</doStatement>" in filep[k]:
        return 122
    if "<returnStatement>" in filep[k]:
        return 123
    if "</returnStatement>" in filep[k]:
        return 124
    if "<expression>" in filep[k]:
        return 125
    if "</expression>" in filep[k]:
        return 126
    if "<term>" in filep[k]:
        return 127
    if "</term>" in filep[k]:
        return 128
    if "<expressionList>" in filep[k]:
        return 129
    if "</expressionList>" in filep[k]:
        return 130


def compilevardec():
    global vmv
    global local_count, argument_count, total_count, currentsubroutinename
    if check(vmv) == 111:  # vardec
        vmv = vmv + 1
    else:
        print("error31")
        return
    if check(vmv) == 10:  # var
        vmv = vmv + 1
    else:
        print("error32")
        return
    if check(vmv) == 11 or check(vmv) == 12 or check(vmv) == 13 or check(vmv) == 3:
        type = extract(vmv).split()[0]
        vmv = vmv + 1
    else:
        print("error33")
        return
    if check(vmv) == 3:
        varname = extract(vmv).split()[0]
        vmv = vmv + 1
    else:
        print("error34")
        return
    subroutine_symbol_table.append(variable(varname, type, "local", local_count))
    local_count += 1
    total_count += 1
    while check(vmv) == 33:
        vmv = vmv + 1
        if check(vmv) == 3:
            varname = extract(vmv).split()[0]
            vmv = vmv + 1
        else:
            print("error36" + filep[vmv - 1])
            return
        subroutine_symbol_table.append(variable(varname, type, "local", local_count))
        local_count += 1
        total_count += 1
    if check(vmv) == 34:  # ';'
        vmv = vmv + 1
    else:
        print("error37")
    if check(vmv) == 112:  # /vardec
        vmv = vmv + 1
    else:
        print("error38")


def compilesubroutinedec():
    global vmv
    global static_count_cls, total_count_cls, field_count_cls
    global kind, type, varname
    global local_count, argument_count, total_count, currentsubroutinename, currentsubroutinetype
    global class_symbol_table, subroutine_symbol_table

    if check(vmv) == 105:  # subroutine dec
        vmv = vmv + 1
    else:
        print("error21")
        return
    if check(vmv) == 5 or check(vmv) == 6 or check(vmv) == 7:  # 'constructor' 'func' 'method'
        kind = extract(vmv).split()[0]
        vmv = vmv + 1
    else:
        print("error22")
        return
    if check(vmv) == 11 or check(vmv) == 12 or check(vmv) == 13 or check(vmv) == 14 or check(
            vmv) == 3:  # 'int' 'char' 'bool' 'void' ' identifer
        type = extract(vmv).split()[0]
        vmv = vmv + 1
    else:
        print("error23")
        return
    if check(vmv) == 3:  # 'identifier'
        varname = extract(vmv).split()[0]
        vmv = vmv + 1
    else:
        print("error24")
        return
    local_count = 0
    argument_count = 0
    total_count = 0
    subroutine_symbol_table = []
    currentsubroutinename = varname
    currentsubroutinetype = kind

    if kind == "method":
        subroutine_symbol_table.append(variable("this", "argument", currentclassname, 0))
        argument_count += 1
        total_count += 1
    if check(vmv) == 28:  # '('
        vmv = vmv + 1
    else:
        print("error25")
        return
    print("para")
    print(str(argument_count) + "argument")
    if check(vmv) == 107:
        compileparameterlist()
    if check(vmv) == 29:  # ')'
        vmv = vmv + 1
    else:
        print("error26")
        return
    print("sub")
    if check(vmv) == 109:  # sbroutinebody
        compilesubroutinebody()
    if check(vmv) == 106:  # /subroutinedec
        vmv = vmv + 1
    else:
        print("error27")
        return


def compileclassvardec():
    global vmv
    global static_count_cls, total_count_cls, field_count_cls
    global kind, type, varname
    if check(vmv) == 103:  # classvardec
        vmv = vmv + 1
    else:
        print("error41")
        return
    if check(vmv) == 8 or check(vmv) == 9:  # '1
        # ' 'static'
        kind = extract(vmv).split()[0]
        vmv = vmv + 1
    else:
        print("error42")
        return
    if check(vmv) == 11 or check(vmv) == 12 or check(vmv) == 13 or check(vmv) == 3:  # 'char' 'int' 'bool' identifer
        type = extract(vmv).split()[0]
        vmv = vmv + 1
    else:
        print("error43")
        return
    if check(vmv) == 3:  # identifier
        varname = extract(vmv).split()[0]
        vmv = vmv + 1
    else:
        print("error44")
        return
    if kind == "static":
        class_symbol_table.append(variable(varname, type, kind, static_count_cls))
        static_count_cls += 1
        total_count_cls += 1
    else:
        class_symbol_table.append(variable(varname, type, kind, field_count_cls))
        field_count_cls += 1
        total_count_cls += 1
    if check(vmv) == 33:
        while check(vmv) == 33:
            vmv = vmv + 1
            if check(vmv) == 3:
                varname = extract(vmv).split()[0]
                vmv = vmv + 1
                if kind == "static":
                    class_symbol_table.append(variable(varname, type, kind, static_count_cls))
                    static_count_cls += 1
                    total_count_cls += 1
                else:
                    class_symbol_table.append(variable(varname, type, kind, field_count_cls))
                    field_count_cls += 1
                    total_count_cls += 1
            else:
                print("error46")
                return
    if check(vmv) == 34:  # ';'
        vmv = vmv + 1
    else:
        print("error47")
        return
    if check(vmv) == 104:  # /classvardec
        vmv = vmv + 1
    else:
        print("error48")
        return


def compileclass():
    global vmv, varname
    global currentclassname, total_count_cls, field_count_cls, static_count_cls, class_symbol_table
    if check(vmv) == 101:
        vmv = vmv + 1
    else:
        print("error7")
    if check(vmv) == 0:
        vmv = vmv + 1
    else:
        print("error8")
    if check(vmv) == 3:
        varname = extract(vmv)
        print(varname)
        vmv = vmv + 1
    else:
        print("error9")
    if check(vmv) == 26:
        vmv = vmv + 1
    else:
        print("error11")
    class_symbol_table = []
    field_count_cls = 0
    static_count_cls = 0
    total_count_cls = 0
    # print("varnamr=" + varname)
    currentclassname = varname
    if check(vmv) == 103:
        while check(vmv) == 103:
            print('hh\n')
            compileclassvardec()
    if check(vmv) == 105:
        while check(vmv) == 105:
            print("jj\n")
            compilesubroutinedec()
    if check(vmv) == 27:
        vmv = vmv + 1
    else:
        print("error12")
    if check(vmv) == 102:
        vmv = vmv + 1
    else:
        print("error13")


def compilesubroutinebody():
    global vmv, currentclassname, currentsubroutinename, local_count, field_count_cls, currentsubroutinetype
    if check(vmv) == 109:  # subroutinebody
        vmv = vmv + 1
    else:
        print("error1")
        return
    if check(vmv) == 26:  # '{'
        vmv = vmv + 1
    else:
        print("error2")
        return
    if check(vmv) == 111:  # vardec
        while check(vmv) == 111:
            print("vardec")
            compilevardec()
    # print("cagde=" + currentclassname)
    vfile.write("function " + currentclassname + "." + currentsubroutinename + " " + str(local_count) + "\n")
    if currentsubroutinetype == "constructor":
        vfile.write("push constant " + str(field_count_cls) + "\n")
        vfile.write("call Memory.alloc 1\n")
        vfile.write("pop pointer 0\n")
    elif currentsubroutinetype == "method":
        vfile.write("push argument 0\n")
        vfile.write("pop pointer 0\n")
    # print(check(vmv))
    if check(vmv) == 113:  # statements
        # print("state")
        compilestatements()
    else:
        print("error3")
    if check(vmv) == 27:  # '}'
        vmv = vmv + 1
    else:
        print("error4")
    if check(vmv) == 110:  # subroutine
        vmv = vmv + 1
    else:
        print("error5")


def compileparameterlist():
    global vmv, type, varname
    global local_count, argument_count, total_count, currentsubroutinename
    if check(vmv) == 107:  # parameterlist
        vmv = vmv + 1
    else:
        print("error51")
        return
    if check(vmv) == 108:  # /parameterlist
        vmv = vmv + 1
        return
    else:
        if check(vmv) == 11 or check(vmv) == 12 or check(vmv) == 13 or check(vmv) == 3:
            type = extract(vmv).split()[0]
            vmv = vmv + 1
        else:
            print("error52")
            return
        if check(vmv) == 3:
            varname = extract(vmv).split()[0]
            vmv = vmv + 1
        else:
            print("error53")
            return
        subroutine_symbol_table.append(variable(varname, type, "argument", argument_count))
        argument_count += 1
        total_count += 1
        while check(vmv) == 33:
            vmv = vmv + 1
            if check(vmv) == 11 or check(vmv) == 12 or check(vmv) == 13 or check(vmv) == 3:
                type = extract(vmv).split()[0]
                vmv = vmv + 1
            else:
                print("error54")
                return
            if check(vmv) == 3:
                varname = extract(vmv).split()[0]
                vmv = vmv + 1
            else:
                print("error55")
                return
            subroutine_symbol_table.append(variable(varname, type, "argument", argument_count))
            argument_count += 1
            total_count += 1
        if check(vmv) == 108:  # /parameterlist
            vmv = vmv + 1
            return
        else:
            print("error56")
            return


def compileexpression():
    print("expression")
    global vmv
    if check(vmv) == 125:  # expression
        vmv += 1
    if check(vmv) == 127:  # term
        # print("no")
        # print(filep[vmv],vmv)
        compileterm()
    # print(filep[vmv],vmv)
    while check(vmv) == 35 or check(vmv) == 36 or check(vmv) == 37 or check(vmv) == 38 or check(vmv) == 39 or check(
            vmv) == 40 or check(vmv) == 41 or check(vmv) == 42 or check(
        vmv) == 43:  # '+' '-' '*' '/' '&' '|' '<' '>' '='
        if check(vmv) == 35:
            op = "add\n"
        elif check(vmv) == 36:
            op = "sub\n"
        elif check(vmv) == 37:
            op = "call Math.multiply 2\n"
        elif check(vmv) == 38:
            op = "call Math.divide 2\n"
        elif check(vmv) == 39:
            op = "and\n"
        elif check(vmv) == 40:
            op = "or\n"
        elif check(vmv) == 41:
            op = "lt\n"
        elif check(vmv) == 42:
            op = "gt\n"
        elif check(vmv) == 43:
            op = "eq\n"
        vmv += 1
        if check(vmv) == 127:  # term
            compileterm()
        vfile.write(op)

    if check(vmv) == 126:  # /expression
        # print("/expression")
        vmv += 1


def compileexpressionlist():
    # print("expression list")
    global nP
    nP = 0
    global vmv
    # print("explist")
    if check(vmv) == 129:  # expessionlist
        vmv += 1
    if check(vmv) == 125:  # expression
        # print("sdbajeh" + filep[vmv][0:-1])
        compileexpression()
        # print("sac"+filep[vmv][0:-1])
        nP += 1
        while check(vmv) == 33:
            vmv += 1
            if check(vmv) == 125:  # expression
                compileexpression()
                nP += 1
    # print(filep[vmv][0:-1])
    if check(vmv) == 130:  # /expressionlist
        vmv += 1
        # print("/expression list nP=" + str(nP))
        return


def compilestatements():
    print("compstate")
    global vmv
    if check(vmv) == 113:
        vmv = vmv + 1
    else:
        print("error40")
    while check(vmv) == 115 or check(vmv) == 117 or check(vmv) == 119 or check(vmv) == 121 or check(vmv) == 123:
        if check(vmv) == 115:
            # print("115")
            compileletstatement()
        elif check(vmv) == 117:
            compileifstatement()
        elif check(vmv) == 119:
            compilewhilestatement()
        elif check(vmv) == 121:
            compiledostatement()
        elif check(vmv) == 123:
            compilereturnstatement()
    print(filep[vmv])
    if check(vmv) == 114:
        vmv = vmv + 1
        # print("/compstate")
    else:
        print("error29" + filep[vmv - 1][0:-1], str(vmv) + "error29")


def compileletstatement():
    print("let")
    global vmv
    f = 0
    global total_count_cls
    if check(vmv) == 115:  # letstatement
        vmv += 1
    if check(vmv) == 19:  # let
        vmv += 1
    if check(vmv) == 3:  # varname
        varname = extract(vmv)
        print(varname)
        vmv += 1
    c = 0
    for x in subroutine_symbol_table:
        if x.name == varname:
            kind = x.kind
            type = x.type
            index = x.no
            c = 1
            break
    if c == 0:
        for x in class_symbol_table:
            if x.name == varname:
                kind = x.kind
                type = x.type
                index = x.no
                c = 1
                break
    if c == 0:
        print("error : " + varname + "not declared \n")
        return

    if check(vmv) == 30:  # '['
        vmv += 1
        f = 1
        if check(vmv) == 125:  # expression
            compileexpression()
        if check(vmv) == 31:  # ']'
            vmv += 1
        vfile.write("push " + kind + " " + str(index) + "\nadd\n")

    if check(vmv) == 43:  # '='
        vmv += 1
    if check(vmv) == 125:  # expression
        print("ook")
        compileexpression()
    if check(vmv) == 34:  # ';'
        print("ok")
        vmv += 1
    if f == 0:  # without '[exp]'
        vfile.write("pop " + kind + " " + str(index) + "\n")
    else:  # with '[exp]'
        vfile.write("pop temp 0\npop pointer 1\npush temp 0\npop that 0\n")
    print(filep[vmv])
    if check(vmv) == 116:  # /letstatement
        vmv += 1
    print("/let")


def compileifstatement():
    global vmv
    # print("if" + filep[vmv+5][0:-1])
    global label
    tlabel = label
    label += 2
    if check(vmv) == 117:  # ifstatement
        vmv += 1
    if check(vmv) == 21:  # "if"
        vmv += 1
    if check(vmv) == 28:  # '('
        vmv += 1
    if check(vmv) == 125:  # expression
        compileexpression()
    if check(vmv) == 29:  # ')'
        vmv += 1
    vfile.write("not\nif-goto " + currentclassname + ".label" + str(tlabel) + "\n")
    if check(vmv) == 26:  # '{'
        vmv += 1
    if check(vmv) == 113:  # statements
        compilestatements()
    if check(vmv) == 27:  # '}'
        vmv += 1
    vfile.write(
        "goto " + currentclassname + ".label" + str(tlabel + 1) + "\nlabel " + currentclassname + ".label" + str(
            tlabel) + "\n")
    if check(vmv) == 22:  # else
        vmv += 1
        # print("else")
        if check(vmv) == 26:
            vmv += 1
        if check(vmv) == 113:
            compilestatements()

        if check(vmv) == 27:
            vmv += 1
            # print("/else")
    vfile.write("label " + currentclassname + ".label" + str(tlabel + 1) + "\n")
    if check(vmv) == 118:  # /ifstatement
        vmv += 1
    # print("/if")


def compilewhilestatement():
    print("while")
    global vmv
    global label
    tlabel = label
    label += 2
    if check(vmv) == 119:  # whilestatement
        vmv += 1
    if check(vmv) == 23:  # "while"
        vmv += 1
    if check(vmv) == 28:  # '('
        vmv += 1
    vfile.write("label " + currentclassname + ".label" + str(tlabel) + "\n")
    if check(vmv) == 125:  # expression
        compileexpression()
    if check(vmv) == 29:  # ')'
        vmv += 1
    vfile.write("not\nif-goto " + currentclassname + ".label" + str(tlabel + 1) + "\n")
    if check(vmv) == 26:  # '{'
        vmv += 1
    if check(vmv) == 113:  # statements
        compilestatements()
    if check(vmv) == 27:  # '}'
        vmv += 1
    vfile.write("goto " + currentclassname + ".label" + str(tlabel) + "\nlabel " + currentclassname + ".label" + str(
        tlabel + 1) + "\n")
    if check(vmv) == 120:  # /while
        vmv += 1
    print("/while" + filep[vmv][0:-1])


def compilereturnstatement():
    print("return")
    global vmv
    global label
    if check(vmv) == 123:  # returnstatement
        vmv += 1
    if check(vmv) == 24:  # "return"
        vmv += 1
    if check(vmv) == 34:  # ';'
        vfile.write("push constant 0\nreturn\n")
        vmv += 1
    elif check(vmv) == 125:  # expression
        compileexpression()
        vfile.write("return\n")
        if check(vmv) == 34:  # ';'
            vmv += 1
    else:
        pass  # error
    if check(vmv) == 124:  # /returnstatement
        vmv += 1


def compiledostatement():
    print("dostate")
    global vmv, currentclassname, nP

    if check(vmv) == 121:  # dostatement
        vmv += 1
    if check(vmv) == 20:  # do
        vmv += 1
    if check(vmv) == 3:  # identifier
        vmv += 1
    if check(vmv) == 32:  # '.'
        id1 = extract(vmv - 1)  # "classname" or "varname"
        vmv += 1
        if check(vmv) == 3:  # subroutine name
            id2 = extract(vmv)
            vmv += 1
        c = 0
        for x in subroutine_symbol_table:
            if x.name == id1:
                kind = x.kind
                type = x.type
                index = x.no
                c = 1
                break
        if c == 0:
            for x in class_symbol_table:
                if x.name == id1:
                    kind = x.kind
                    type = x.type
                    index = x.no
                    c = 2
                    break
        if c == 2:  # if yes
            vfile.write("push " + kind + " " + str(index) + "\n")
        if check(vmv) == 28:  # '('
            vmv += 1
        if check(vmv) == 129:  # expressionlist
            compileexpressionlist()
        if check(vmv) == 29:  # ')'
            vmv += 1
        if c == 1:
            vfile.write("call " + type + "." + id2 + " " + str(nP + 1) + "\npop temp 0\n")
        else:
            vfile.write("call " + id1 + "." + id2 + " " + str(nP) + "\npop temp 0\n")

    else:  # '('
        id1 = extract(vmv - 1)  # subname
        vfile.write("push pointer 0\n")
        vmv += 1
        if check(vmv) == 129:  # expressionlist
            compileexpressionlist()  # no af arguments
        if check(vmv) == 29:  # ')'
            vmv += 1
            vfile.write("call " + currentclassname + "." + id1 + " " + str(nP + 1) + "\npop temp 0\n")  # remaining

    if check(vmv) == 34:  # ';'
        vmv += 1
    if check(vmv) == 122:  # /dostatement
        vmv += 1


def compileterm():
    global vmv, class_symbol_table, subroutine_symbol_table, nP
    print("compterm" + filep[vmv + 1][0:-1])
    if check(vmv) == 127:  # term
        vmv += 1
    if check(vmv) == 36 or check(vmv) == 44:  # '-' '~'
        if check(vmv) == 36:  # '-'
            op = "neg\n"
            vmv += 1
        elif check(vmv) == 44:  # '~'
            op = "not\n"
            vmv += 1
        if check(vmv) == 127:  # term
            compileterm()
        vfile.write(op)
    elif check(vmv) == 28:  # '('
        vmv += 1
        if check(vmv) == 125:  # expression
            compileexpression()
        if check(vmv) == 29:  # ')'
            vmv += 1
    elif check(vmv) == 4:  # integer constant
        print("intconst")
        integervalue = extract(vmv)
        vmv += 1
        vfile.write("push constant " + integervalue + "\n")
    elif check(vmv) == 15 or check(vmv) == 16 or check(vmv) == 17 or check(vmv) == 18:  # 'true' 'false' 'null' 'this'
        if check(vmv) == 15:  # 'true'
            vfile.write("push constant 0\nnot\n")
        if check(vmv) == 16:  # 'false'
            vfile.write("push constant 0\n")
        if check(vmv) == 17:  # 'null'
            vfile.write("push constant 0\n")
        if check(vmv) == 18:  # 'this'
            vfile.write("push pointer 0\n")
        vmv += 1
    elif check(vmv) == 3 and not (check(vmv + 1) == 28 or check(vmv + 1) == 32):  # 'varname' ([)?
        varname = extract(vmv)
        c = 0
        vmv += 1
        for x in subroutine_symbol_table:
            print("symbtable " + varname + " =? " + x.name)
            if x.name == varname:
                type = x.type
                kind = x.kind
                index = x.no
                c = 1
                break
        if c == 0:
            for x in class_symbol_table:
                print("symbtable " + varname + " =? " + x.name)
                if x.name == varname:
                    type = x.type
                    kind = x.kind
                    index = x.no
                    c = 1
                    break
        if c == 0:
            print("error : " + varname + " not declared\n")
            return
        if check(vmv) == 30:  # '['
            vmv += 1
            if check(vmv) == 125:  # expression
                compileexpression()
            if check(vmv) == 31:  # ']'
                vmv += 1
                vfile.write("push " + kind + " " + str(index) + "\nadd\npop pointer 1\npush that 0\n")
        else:  # not'['
            vfile.write("push " + kind + " " + str(index) + "\n")
    elif check(vmv) == 2:  # stringconstant
        string = extract(vmv)
        strlen = len(string)
        vfile.write("push constant " + str(strlen) + "\ncall String.new 1\n")
        for x in string:
            vfile.write("push constant " + str(ord(x)) + "\ncall String.appendChar 2\n")
        vmv += 1
    elif check(vmv) == 3 and (check(vmv + 1) == 28 or check(vmv + 1) == 32):  # subroutine call
        vmv += 1
        print("subcall\n")
        if check(vmv) == 28:  # '('
            id1 = extract(vmv - 1)
            vmv += 1
            vfile.write("push pointer 0\n")
            if check(vmv) == 129:  # expressionlist
                compileexpressionlist()
            if check(vmv) == 29:  # ')'
                vmv += 1
                vfile.write("call " + currentclassname + "." + id1 + " " + str(nP + 1) + "\n")
        else:  # '.'
            id1 = extract(vmv - 1)  # classname or varname
            # print("id1 = " + id1)
            if check(vmv) == 32:  # '.'
                vmv += 1
            if check(vmv) == 3:  # subroutine name
                id2 = extract(vmv)
                vmv += 1
            c = 0
            for x in subroutine_symbol_table:
                if x.name == id1:
                    type = x.type
                    kind = x.kind
                    index = x.no
                    c = 1
                    break
            if c == 0:
                for x in class_symbol_table:
                    if x.name == id1:
                        type = x.type
                        kind = x.kind
                        index = x.no
                        c = 1
                        break
            if c == 1:
                vfile.write("push " + kind + " " + str(index) + "\n")
            if check(vmv) == 28:  # '('
                vmv += 1
            if check(vmv) == 129:
                compileexpressionlist()
            # print("nP"+filep[vmv] +" nP="+str(nP))
            if check(vmv) == 29:  # ')'
                # print(")"+filep[vmv])
                vmv += 1
            if c == 0:
                vfile.write("call " + id1 + "." + id2 + " " + str(nP) + "\n")
            else:
                vfile.write("call " + id1 + "." + id2 + " " + str(nP + 1) + "\n")
    else:
        print("error : term  " + filep[vmv] + "check= " + check(vmv))
    # print("filev compterm "+filep[vmv],filep[vmv+1]+"/filev compterm")
    if check(vmv) == 128:
        vmv += 1
        print("/compterm")
    else:
        print("term error")
    # print("/compterm")


#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################
def remove(line):
    global flg
    if line == '':
        return ''
    else:
        s = line[0]
    if line[0:2] == "//":
        return ""
    elif line[0:2] == "*/":
        flg = 0
        return line[line.index("*/") + 3:]
    elif line[0:2] == "/*" or flg == 1:
        flg = 1
        if "*/" not in line:
            return ""
        else:
            flg = 0
            return line[line.index("*/") + 2:]
    elif s == "\n":
        return ""
    else:
        return s + remove(line[1:])


def first_pass(f):
    inp = open(f + ".jack", 'r')
    out = open(f + '.ir', 'w')
    for line in inp:
        new_line = remove(line)
        if new_line != "" or new_line != "\n":
            out.write(new_line + "\n")
    inp.close()
    out.close()


##########################################################################################################################
flg = 0
a = "py//"
for u in range(n):
    s = input("file name without '.jack' extention")

    first_pass(s)



    jackj = 0
    jackt = 0
    flag = 0

    with open(s + ".ir", 'r') as filejac:
        jackfile = filejac.readlines()
    i = len(jackfile)
    filepars = open(s + "T.xml", 'w')
    filepars.write("<token>\n")


    for v in range(i):
        jackj = v
        # print("\n")
        jackt = 0
        if flag == 1:
            comment(v)
        else:
            checkjack(v)
    filepars.write("</token>\n")
    filepars.close()
#################################################
    parsv = 0
    space = 0

    with open(s + "T.xml", 'r') as file1:
        filecontent = file1.readlines()
    kfile = open(s + ".xml", 'w')
    print("s="+s)
    parse()
    kfile.close()
##################################################
    vmv = 0
    label = 0
    field_count_cls = 0
    static_count_cls = 0
    total_count_cls = 0
    local_count = 0
    total_count = 0
    argument_count = 0
    subroutine_symbol_table = []
    class_symbol_table = []
    currentclassname = ""
    currentsubroutinename = ""
    currentsubroutinetype = ""

    with open(s + ".xml", 'r') as file1:
        filep = file1.readlines()
    vfile = open(s + ".vm", 'w')

    main()

    vfile.close()
######################################################    