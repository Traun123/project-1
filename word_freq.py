import string


def read_file(file_path):
    try:
        with open(file_path,'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.Please Provide a Valid file path.")
        return ""
    

def process_text(text):
    #remove punctuation and convert to lowercase
    text=text.translate(str.maketrans('','',string.punctuation))
    words=text.Lowere().split()
    return words

def count_word_frequency(words):
    word_frequency ={}
    for word in words:
        word_frequency[word]=word_frequency.get(word,0)+1
    return word_frequency

def display_word_frequency(word_frequency):
    print("word_frequency:")
    for word,count in word_frequency.items():
        print(f"{word}: {count}")

if __name__=="__main__":
    try:
        file_path = input("Enter the path of the text file:")
        text = read_file(file_path)

        if text:
            words = process_text(text)
            word_frequency = count_word_frequency(words)
            display_word_frequency(word_frequency)
    except KeyboardInterrupt:
        print("\nprogram interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    