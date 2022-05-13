from tempfile import NamedTemporaryFile
from os import listdir
import shutil
import csv

topics = listdir("topic_CSVS")

for topic in topics:
    filename = "topic_CSVS/" + topic
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        writer = csv.writer(tempfile, delimiter=',', quotechar='"')
        #columns = ["main_topic", "description_1", "bill_link", "bill_name", "current_status", "house_progress",
        #           "senate_progress", "after_passage_progress", "description_2", "sponsors", "requester"]
        #writer.writerow(columns)
        for row in reader:
            if len(row) == 13:
                #sponsors = row[9]
                #sponsors = sponsors.replace("Johnson, J.", "Jesse Johnson")
                #sponsors = sponsors.replace("Wilson, C.", "Claire Wilson")
                #sponsors = sponsors.replace("Wilson, J.", "Jeff Wilson")
                #sponsors = sponsors.replace("Wilson, L.", "Linda Wilson")
                #row[9] = sponsors
                if "['0','0','0','0']" in row[5]:
                    row[5] = "['1','0','0','0']"
                if "['0','0']" in row[7]:
                    row[7] == "['1', '1', '1', '0']"
                if row[4] == "ov vetoed":
                    row[4] = "Gov vetoed"
                writer.writerow(row)

    shutil.move(tempfile.name, filename)

members = listdir("member_CSVS")

for member in members:
    filename = "member_CSVS/" + member
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        writer = csv.writer(tempfile, delimiter=',', quotechar='"')

        #columns = ["name", "party"]
        #writer.writerow(columns)

        for row in reader:
            writer.writerow(row)

    shutil.move(tempfile.name, filename)
