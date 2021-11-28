def sort_sentence(sentence):

    sentence = sentence.lower()
    final = sentence.split()

    sortsent = sorted(final, key=len)

    string = " ".join(sortsent)

    return string.capitalize()
