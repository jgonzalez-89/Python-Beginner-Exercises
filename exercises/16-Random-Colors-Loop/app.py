import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():
    color_array = []
    students_array = []
    #your loop here
    for i in range(10):
        students_array.append(random.randint(0, 3))
    for color in students_array:
        color_array.append(get_color(color))
    return color_array

get_allStudentColors()