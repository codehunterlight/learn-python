import easyocr


def text_recognition(file_path, text_file_name):
    reader = easyocr.Reader(['en'])                 # Choice analyze language
    result = reader.readtext(file_path)             # Run analyze image

    # Write in result.txt file analyzed text with image
    with open(text_file_name, 'w') as file:
        for line in result:
            file.write(f'{line}')

    # Output operation good finished
    return f'Result saved in {text_file_name}'


def main():
    file_path = 'lorem.png'
    text_file_name = 'result.txt'
    print(text_recognition(file_path, text_file_name))


main()
