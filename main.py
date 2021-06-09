"""Pre-filtering an RR range export file
     1- Remove the minimum values until they are repeated
     2- Removes the maximum values until they are repeated
     3- If necessary (for the Polar device), convert the values to milliseconds and exclude the accumulated time
     4- creates a pre-filtered txt file with RR intervals
     5- Creates a file with the first 256 pre-filtered RR intervals, if there are enough intervals
     6- Creates a file with the first 1000 pre-filtered RR intervals, if there are enough intervals
    """

import os
from os import listdir
from os.path import isfile, join


def main():
    path = 'files/SamplePolar'
    device = 1  # Device used: 1 = PolarV800 | 2 = EliteHRV

    """scan files in the directory"""
    for f in listdir(path):
        if isfile(join(path, f)):
            file = join(path, f)
            hrv_input = read_txt(file).splitlines()
            hrv_output = pre_filter(hrv_input, device)
            hrv_output_256 = []
            hrv_output_1000 = []

            '''Creation of pre-filtered original file'''
            name = '{}_pre_filtered.txt'.format(os.path.splitext(file)[0])
            create_output(hrv_output, name)

            '''Creation of pre-filtered file with the first 256 RR intervals, if there are enough intervals'''
            if len(hrv_output) > 256:
                name = '{}_pre_filtered_256.txt'.format(os.path.splitext(file)[0])
                for i in range(256):
                    hrv_output_256.append(hrv_output[i])
                create_output(hrv_output_256, name)

            '''Creation of the pre-filtered file with the first 1000 RR intervals, if there are enough intervals'''
            if len(hrv_output) > 1000:
                name = '{}_pre_filtered_1000.txt'.format(os.path.splitext(file)[0])
                for i in range(1000):
                    hrv_output_1000.append(hrv_output[i])
                create_output(hrv_output_1000, name)


'''Read file'''
def read_txt(file):
    hrv_input = open(file, 'r')
    return hrv_input.read()


"""Pre-filtering"""
def pre_filter(input, device):
    work = []
    """Defines the input file type"""
    if device == 1:
        for i, number in enumerate(input):
            work.append(round((float(number.split()[1]) * 1000)))
    else:
        work = input
    """Remove minimum values until there is a repeated minimum value"""
    while True:
        n_out = min(work)
        if work.count(n_out) == 1:
            work.remove(n_out)
        else:
            break
    """Remove maximum values until there is a repeated maximum value"""
    while True:
        n_out = max(work)
        if work.count(n_out) == 1:
            work.remove(n_out)
        else:
            break
    return work


"""Output file creation"""
def create_output(file, name):
    file_output = open(name, 'w')
    for i in file:
        file_output.write("{}\n".format(i))
    file_output.close()


if __name__ == "__main__":
    main()
