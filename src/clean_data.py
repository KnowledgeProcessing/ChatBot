from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super(MLStripper, self).__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


filenames = {
    "train.a": "train.en",
    "train.b": "train.fr"
}


def remove_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


for in_filename, out_filename in filenames.items():
    with open(in_filename, "r") as in_file:
        with open(out_filename, "w") as out_file:
            for line in in_file:
                out_file.write(remove_tags(line))
