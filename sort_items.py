import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    # file_path = os.path.join(cwd_path, file_name)
    file_name = "numbers_one.CSV"
    with open(file_name, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter='\t')
        for line in data:
            line = [int(number) for number in line]
        return line


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    with open(file_name,"r") as csvfile:
        data = csv.reader(csvfile)

        for line_index, line in enumerate(data):
            if line_index == row_number:
                row = [int(number) for number in line]

        return row

def selection_sort(number_array, direction = "<"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    for count, _ in enumerate(number_array):
        minimum = count
        for number_index, number in enumerate(number_array[count:]):
            if direction == "<":
                if number < number_array[minimum]:
                    minimum = number_index + count
            elif direction == ">":
                if number > number_array[minimum]:
                    minimum = number_index + count

        number_array[count], number_array[minimum] = number_array[minimum],  number_array[count]
    return number_array




def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    for index in range(len(number_array) - 1):
        for index_2 in range(0,len(number_array) - 1 - index):
            if number_array[index_2] > number_array[index_2 + 1]:
                number_array[index_2], number_array[index_2 + 1] = number_array[index_2 + 1],  number_array[index_2]

    return number_array


def main():

    # Ukol: Selection Sort
    file_name = "numbers_one.CSV"
    func = read_row(file_name)


    # Ukol: Selection Sort - se smerem razeni
    sort_1 = selection_sort(func)

    # Ukol: Bubble Sort
    funkce_2 = read_rows("numbers_two.CSV", 1)

    sort_2 = bubble_sort(funkce_2)
    print(sort_2)

    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

