import re
import csv



with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    format_list = []


def format_name():
    for column in contacts_list:
        data = column[0].split(' ')
        if len(data) > 1:
            column[0] = data[0]
            column[1] = data[1]
            if len(data) > 2:
                column[2] = data[2]

        data = column[1].split(' ')
        if len(data) > 1:
            column[1] = data[0]
            column[2] = data[1]
    return


def format_num():
    number_pattern_raw = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    number_pattern_new = r'+7(\2)\3-\4-\5\7\8\9'
    for column in contacts_list:
        column[5] = number_pattern_raw.sub(number_pattern_new, column[5])
    return


def duplicates():
    for column in contacts_list[1:]:
        first_name = column[0]
        last_name = column[1]
        for contact in contacts_list:
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if column[2] == '':
                    column[2] = contact[2]
                if column[3] == '':
                    column[3] = contact[3]
                if column[4] == '':
                    column[4] = contact[4]
                if column[5] == '':
                    column[5] = contact[5]
                if column[6] == '':
                    column[6] = contact[6]
    for contact in contacts_list:
        if contact not in format_list:
            format_list.append(contact)
    return format_list


if __name__ == '__main__':

    format_name()
    format_num()
    duplicates()

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(format_list)
