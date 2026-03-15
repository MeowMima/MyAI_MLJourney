#File Objects - Reading & Writing to Files

#When the file is in the same directory
"""
f = open('SampleText.txt', 'r')
print(f.mode)
f.close()
"""
#In Context Manager - best practice(automatic clean up/closing file)
with open('SampleText.txt', 'r') as f:
    """
    f_contents = f.read()  #this loads the content of the file in the memory
    print(f_contents)
    
    f_contents = f.readlines() #this will make a list out of the contents
    print(f_contents)

    f_contents = f.readline() #this will just read the first line of the file
    print(f_contents)

    f_contents = f.readline() #next line of the file content will be printed in a new line
    print(f_contents)

    #To read the contents of the file without utilising or overcrwoding the memory space - readline() method can be used in iteration
    for line in f:
        print(line, end = '')

    #To read a selected/specific content in the file
    f_contents = f.read(20)  #read first '5' characters of the file
    print(f_contents, end = '')

    """
    """
     #To read a Large File - iterating small chunks
    size_to_read = 10   #initializing the no. of characters to be read
    f_contents = f.read(size_to_read)      #method for reading the contents of the file

    while (len(f_contents) > 0):           #'while' loop- i.e. the process will run at least once before checking the cond
        print(f_contents, end = '*')        #now printing the output
        f_contents = f.read(size_to_read)  #again checking the cond or else remember: the length of the contents of the file will always be greater than '0' thus entering an inf loop 
    
    #tell() and seek() methods - 
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)
    print(f.tell())   #tell where the pointer is currently while reading
    f.seek(10)        #to seek the content of the file 'from' the character we want to
    f_contents = f.read(size_to_read)
    print(f_contents)
    """

#WRITING TO THE FILES
with open('SampleText2.txt', 'w') as f:
    f.write("We are creating and writing to a new file \nThe file will be a 'text' file \nIt will be formed in the same directory as my current folder")

#READING & WRITING TO A FILE
with open('SampleText.txt', 'r') as rf:
    with open('CopyFile.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

#LET US WORK WITH AN IMAGE FILE
with open('SampleImage.jpg', 'rb') as imgR:
    with open('CopyImage.jpg', 'wb') as imgW:
        chunk_size = 100
        imgR_chunk = imgR.read(chunk_size)

        while (len(imgR_chunk)>0) :
            imgW.write(imgR_chunk)
            imgR_chunk = imgR.read(chunk_size)
            