import pprint

class GTFS:
    '''
    GTFS Class for storing data from CATA
    '''

    def __init__(self, name, filename):
        '''
        Initializes a GTFS object
        '''

        self.id = name
        self.body = []

        # Read data from file
        infile = open(filename, "r")
        for line in infile:
            data = line[:-1].split(",")

            # Record column data
            if hasattr(self, "header"):
                for n, info in enumerate(data):
                    try:
                        self.body[n].append(info)

                    except IndexError as e:
                        pass


            # Record column names
            else:
                self.header = []
                for info in data:
                    self.header.append(info)
                    self.body.append([])

        infile.close()

    def display(self):
        pp = pprint.PrettyPrinter(indent = 4)
        print()
        print(self.id)
        print(self.header)
        print()
        #pp.pprint(self.body)
        for column in self.body:
            print(column)
        print()


def main():
    files = ["agency.txt", "calendar.txt", "calendar_dates.txt",
             "feed_info.txt", "routes.txt", "shapes.txt"]

    for name in files:
        #if name == "routes.txt": #for debugging
        feed_object = GTFS(name[:-4], "./15-05/" + name)
        feed_object.display()


main()
