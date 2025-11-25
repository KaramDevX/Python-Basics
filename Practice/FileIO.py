def easy_task():
    with open("/Users/karamhamad/Desktop/Python/Practice/Text_Files/easy.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{str(i)}\n")
    with open("/Users/karamhamad/Desktop/Python/Practice/Text_Files/easy.txt") as file:
        for x in file:
            print(x.replace("\n", ""))

# Improvements, use x.strip() instead of replace, and remove str(i) within f-string

def easy_task_s():
    with open("/Users/karamhamad/Desktop/Python/Practice/Text_Files/easy.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{i}\n")
    with open("/Users/karamhamad/Desktop/Python/Practice/Text_Files/easy.txt") as file:
        for x in file:
            print(x.strip())
#_______________________________________

def medium_task():
    with open("/Users/karamhamad/Desktop/Python/Practice/Text_Files/medium.txt") as f:
        word = []
        words = []
        unique_words = []
        repeated_words = []
        punctuation = [".", ",", ":", ";", "\'", "\"", "?", "!"]
        for line in f:
            for char in line:
                if char == " " or char == "\n":
                    words.append("".join(word))
                    word = []
                    continue
                elif char in punctuation:
                    continue
                word.append(char)
        for i in words: 
            if i.lower() in unique_words:
                repeated_words.append(i.lower())
            unique_words.append(i.lower())
        unique_words = list(set(unique_words) - set(repeated_words))
        return unique_words
# Improvements, literally everything same improvements for hard task
def medium_task():
    with open("medium.txt") as f:
        words = []
        for line in f:
            for w in line.split():
                w = w.strip(".,:;!?").lower()
                words.append(w)
    # Count occurrences manually
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    # Keep only words that appear once
    unique_words = [word for word, count in counts.items() if count == 1]
    return unique_words

#______________________________
def hard_task():
    with open("/Users/karamhamad/Desktop/Python/Practice/Text_Files/hard.txt") as f: 
        word = []
        names = []
        actions = []
        log = {}
        # Adding all names and actions from log into names and actions lists
        for line in f:
            for char in line:
                if char == " ":
                    names.append("".join(word))
                    word = []
                    continue
                elif char == "\n":
                    actions.append("".join(word))
                    word = []
                    continue
                word.append(char)
            # In case no \n at the end of the file, last action is appended
            if len(names) != len(actions):
                actions.append("".join(word))
        # Adding names and actions into dictionary -> log
        for i, name in enumerate(names):
            if name in log:
                if actions[i] in log[name]:
                    log[name].update({actions[i]: log[name][actions[i]] + 1})
                else:
                    log[name].update({actions[i]: 1})
            else:
                log.update({name: {actions[i]: 1}})
        # printing the log
        for i in log:
            print(i, log[i])


# easy_task()
# print(medium_task())
# hard_task()
