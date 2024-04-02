class TextAnalyzer(object):

    def __init__(self, text):
        # remove punctuation
        formatted_text = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # make text lowercase
        formatted_text = formatted_text.lower()

        self.fmtText = formatted_text

    def freq_all(self):
        # split string into a list
        word_list = self.fmtText.split()

        # creating new dict with all freqs
        word_freq = {}
        for word in set(word_list):
            word_freq[word] = self.fmtText.count(word)
        return word_freq

    def freq_of(self, word):
        return self.fmtText.count(word)

    def freq_of2(self, word):
        # get frequency map
        freq_dict = self.freq_all()

        if word in freq_dict:
            return freq_dict[word]
        else:
            return 0


givenstring = ("Lorem ipsum dolor! diam amet, consetetur Lorem magna."
               " sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
analyzed = TextAnalyzer(givenstring)
print(f"formatted text: {analyzed.fmtText}")
print(analyzed.freq_all())
print(analyzed.freq_of("liad"))
