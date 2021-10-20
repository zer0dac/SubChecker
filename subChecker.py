import optparse

import requests


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--input", dest="input", help="input for file")
    return parse_object.parse_args()


def subcheck(input):
    file1 = open(input, 'r')
    Lines = file1.readlines()
    count = 0
    count2 = 0
    for line in Lines:
        try:
            a: str = ('https://{0}'.format(line.strip()))
            r = requests.get(a)

            if r.status_code != 404:
                print(a)
                count += 1
        except:
            count2 += 1
    print("Reachable websites count are: " + str(count))
    print("Unreachable websites count are: " + str(count2))


print("Sub Checker Started!! ")
(user_input, arguments) = get_user_input()
subcheck(user_input.input)
