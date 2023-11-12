import re
def Open(file_name, mode):

    try:

        file = open(file_name, mode)

    except:

        print("File", file_name, "wasn't opened!")

        return None

    else:

        print("File", file_name, "was opened!")

        return file

file1_name = "TF20_1.txt"

file2_name = "TF20_2.txt"

file_1_w = Open(file1_name, "w")

if file_1_w != None:

    file_1_w.write("Firstly, in a first language the differences are unimportant as people learn their mother tongue naturally, abandonment, advertising, conjuncture, calculation")

    print("Information was succesfully added to TF20_1.txt!")

    file_1_w.close();

    print("File TF20_1.txt was closed!")

file_1_r = Open(file1_name, "r")
file_2_r = Open(file2_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r != None or file_2_w != None or file_2_r != None:

    words = re.split(r'[ ,.?!\n]+', file_1_r.read())
    max=len(max(words,key=len))
    for word in words:
        if len(word)==max:
            file_2_w.write(word+" ")
    file_1_r.close()
    file_2_r.close()
    file_2_w.close()

    print("Files were closed!")

file_3_r = Open(file2_name, "r")

if file_3_r != None:
    out=file_3_r.read().split(" ")
    print("Слова з файлу TF20_2.txt в рядках по 5 слів:")
    i=1
    for word in out:
        
        if word!="":
            print(word, end=" ")
        if i%5==0:
            print()
        i+=1
    print()    
       

    print("File TF20_2.txt was closed!")

    file_3_r.close()