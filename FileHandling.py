# with will flush the data from ram to disk and close the file handle

def create_new_file(statement: str) -> None:
    """
    This function will attempt to create new file with the name
    if already exists it raise an exception and fall back to except clause
    which will overwrite the file and insert the statement
    :param statement:
    :return:
    """
    try:
        with open('myfile.txt', 'x') as file:
            file.write(statement)
    except FileExistsError as exp:
        with open('myfile.txt', 'w') as file:
            file.write(statement)
            file.writelines(['hello\n', 'hola\n', 'hi\n', 'howdy\n', 'happy\n'])
            file.flush()  # Forces the content to be written to the file

def append_the_text(statement: str) -> None:
    """
    If file was not there it will create new file and add the text to it
    further text to the file will be appeneded
    :param statement: string which will inserted into the file
    :return: None
    """
    with open('myfiles.txt', 'a') as file:
        file.write(statement)

def read_the_text() -> None:
    """
    Read the data from file and print it
    :return:
    """
    with open('myfile.txt', 'r') as file:
        text = file.read()  # file.read(n) reads n no.of characters
    print(text)

    with open('myfile.txt', 'r') as file:
        text = file.readlines()  # file.readline() only get one line at a time
        print(text)

def seek_and_tell() -> None:
    with open('myfile.txt', 'r') as file:
        file.seek(6)  # Moves the pointer to the 10th byte
        print(file.read(5))  # Reads the next 5 bytes
        print(file.tell())

def modify_file_size(size: int) -> None:
    with open('myfile.txt', 'r+') as file:
        file.truncate(size)

def main() -> None:
    create_new_file('Hello, world!\n')
    append_the_text('testing sample text\n')
    read_the_text()
    seek_and_tell()
    modify_file_size(30)

if __name__ == '__main__':
    main()

