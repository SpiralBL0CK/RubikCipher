#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

def init_cube(array):
    b = 1
    for i in range(6):
        for j in range(3):
            for k in range(3):
                array[i][j][k] = b
                b += 1   

def rotate_up_right(array):
    temp_value = [array[0][0][2],array[0][1][2],array[0][2][2]]

    array[0][0][2] = array[1][0][2]
    array[0][1][2] = array[1][1][2]
    array[0][2][2] = array[1][2][2]

    array[1][0][2] = array[2][0][2]
    array[1][1][2] = array[2][1][2]
    array[1][2][2] = array[2][2][2]

    array[2][0][2] = array[3][0][2]
    array[2][1][2] = array[3][1][2]
    array[2][2][2] = array[3][2][2]

    array[3][0][2] = temp_value[0]
    array[3][1][2] = temp_value[1]
    array[3][2][2] = temp_value[2]
    
def rotate_up_right_prime(array):
    temp_value_first_set = [array[0][0][2],array[0][1][2],array[0][2][2]]
    array[0][0][2] = array[3][0][2]
    array[0][1][2] = array[3][1][2]
    array[0][2][2] = array[3][2][2]

    temp_value_second_set = [array[1][0][2],array[1][1][2],array[1][2][2]]

    array[1][0][2] = temp_value_first_set[0]
    array[1][1][2] = temp_value_first_set[1]
    array[1][2][2] = temp_value_first_set[2]
    
    temp_value_third_set = [array[2][0][2],array[2][1][2],array[2][2][2]]    

    array[2][0][2] = temp_value_second_set[0]
    array[2][1][2] = temp_value_second_set[1]
    array[2][2][2] = temp_value_second_set[2]

    array[3][0][2] = temp_value_third_set[0]
    array[3][1][2] = temp_value_third_set[1]
    array[3][2][2] = temp_value_third_set[2]	    

def rotate_up_left(array):
    temp_value = [array[0][0][0],array[0][1][0],array[0][2][0]]
    array[0][0][0] = array[1][0][0]
    array[0][1][0] = array[1][1][0]
    array[0][2][0] = array[1][2][0]

    array[1][0][0] = array[2][0][0]
    array[1][1][0] = array[2][1][0]
    array[1][2][0] = array[2][2][0]

    array[2][0][0] = array[3][0][0]
    array[2][1][0] = array[3][1][0]
    array[2][2][0] = array[3][2][0]

    array[3][0][0] = temp_value[0]
    array[3][1][0] = temp_value[1]
    array[3][2][0] = temp_value[2]

def rotate_up_left_prime(array):
    temp_value = [array[0][0][0],array[0][1][0],array[0][2][0]]
    array[0][0][0] = array[3][0][0]
    array[0][1][0] = array[3][1][0]
    array[0][2][0] = array[3][2][0]

    temp_value_set_one = [array[1][0][0],array[1][1][0],array[1][2][0]]
    array[1][0][0] = temp_value[0]
    array[1][1][0] = temp_value[1]
    array[1][2][0] = temp_value[2]
    
    temp_value_set_two = [array[2][0][0],array[2][1][0],array[2][2][0]]
    array[2][0][0] = temp_value_set_one[0]
    array[2][1][0] = temp_value_set_one[1]
    array[2][2][0] = temp_value_set_one[2]

    array[3][0][0] = temp_value_set_two[0]
    array[3][1][0] = temp_value_set_two[1]
    array[3][2][0] = temp_value_set_two[2]

def rotate_up(array):
    temp_value = [array[0][0][0],array[0][0][1],array[0][0][2]]
    array[0][0][0] = array[5][0][0]
    array[0][0][1] = array[5][0][1]
    array[0][0][2] = array[5][0][2]

    temp_value_set_two = [array[4][0][0],array[4][0][1],array[4][0][2]]
    array[4][0][0] = temp_value[0]
    array[4][0][1] = temp_value[1]
    array[4][0][2] = temp_value[2]

    temp_value_set_three = [array[2][0][0],array[2][0][1],array[2][0][2]]
    array[2][0][0] = temp_value_set_two[0]
    array[2][0][1] = temp_value_set_two[1]
    array[2][0][2] = temp_value_set_two[2]

    array[5][0][0] = temp_value_set_three[0]
    array[5][0][1] = temp_value_set_three[1]
    array[5][0][2] = temp_value_set_three[2]

def rotate_up_prime(array):
    temp_value = [array[5][0][0],array[5][0][1],array[5][0][2]]
    array[5][0][0] = array[0][0][0]
    array[5][0][1] = array[0][0][1]
    array[5][0][2] = array[0][0][2]

    temp_value_set_two = [array[2][0][0],array[2][0][1],array[2][0][2]]
    array[2][0][0] = temp_value[0]
    array[2][0][1] = temp_value[1]
    array[2][0][2] = temp_value[2]

    temp_value_set_three = [array[4][0][0],array[4][0][1],array[4][0][2]]
    array[4][0][0] = temp_value_set_two[0]
    array[4][0][1] = temp_value_set_two[1]
    array[4][0][2] = temp_value_set_two[2]

    array[0][0][0] = temp_value_set_three[0]
    array[0][0][1] = temp_value_set_three[1]
    array[0][0][2] = temp_value_set_three[2]

def rotate_front(array):
    temp_value = [array[4][0][0],array[4][1][0],array[4][2][0]]
    array[4][0][0] = array[3][2][0]
    array[4][1][0] = array[3][2][1]
    array[4][2][0] = array[3][2][2]
    
    temp_value_set_two = [array[1][0][0],array[1][0][1],array[1][0][2]]
    array[1][0][0] = temp_value[0]
    array[1][0][1] = temp_value[1]
    array[1][0][2] = temp_value[2]

    temp_value_set_three = [array[5][0][2],array[5][1][2],array[5][2][2]]
    array[5][0][2] = temp_value_set_two[0]
    array[5][1][2] = temp_value_set_two[1]
    array[5][2][2] = temp_value_set_two[2]

    array[3][2][0] = temp_value_set_three[0]
    array[3][2][1] = temp_value_set_three[1]
    array[3][2][2] = temp_value_set_three[2]

def rotate_prime_front(array):
    temp_value = [array[5][0][2],array[5][1][2],array[5][2][2]]
    array[5][0][2] = array[3][2][0]
    array[5][1][2] = array[3][2][1]
    array[5][2][2] = array[3][2][2]

    temp_value_set_two = [array[1][0][0],array[1][0][1],array[1][0][2]]
    array[1][0][0] = temp_value[0]
    array[1][0][1] = temp_value[1]
    array[1][0][2] = temp_value[2]

    temp_value_set_three = [array[4][0][0],array[4][1][0],array[4][2][0]]
    array[4][0][0] = temp_value_set_two[0]
    array[4][1][0] = temp_value_set_two[1]
    array[4][2][0] = temp_value_set_two[2]

    array[3][2][0] = temp_value_set_three[0]
    array[3][2][1] = temp_value_set_three[1]
    array[3][2][2] = temp_value_set_three[2]
    
def rotate_back(array):
    temp_value = [array[5][0][0],array[5][1][0],array[5][2][0]]
    array[5][0][0] = array[3][0][0]
    array[5][1][0] = array[3][1][0]
    array[5][2][0] = array[3][2][0]

    temp_value_set_two = [array[1][2][0],array[1][2][1],array[1][2][2]]

    array[1][2][0] = temp_value[0]
    array[1][2][1] = temp_value[1]
    array[1][2][2] = temp_value[2]

    temp_value_set_three = [array[4][0][2],array[4][1][2],array[4][2][2]]
    array[4][0][2] = temp_value_set_two[0]
    array[4][1][2] = temp_value_set_two[1]
    array[4][2][2] = temp_value_set_two[2]

    array[3][0][0] = temp_value_set_three[0]
    array[3][0][1] = temp_value_set_three[1]
    array[3][0][2] = temp_value_set_three[2]

def rotate_back_prime(array):
    temp_value = [array[4][0][2],array[4][1][2],array[4][2][2]]
    array[4][0][2] = array[3][0][0]
    array[4][1][2] = array[3][0][1]
    array[4][2][2] = array[3][0][2]

    temp_value_set_two = [array[1][2][0],array[1][2][1],array[1][2][2]]
    array[1][2][0] = temp_value[0] 
    array[1][2][1] = temp_value[1]
    array[1][2][2] = temp_value[2]

    temp_value_set_three  = [array[5][0][0],array[5][1][0],array[5][2][0]]
    array[5][0][0] = temp_value_set_two[0]
    array[5][1][0] = temp_value_set_two[1]
    array[5][2][0] = temp_value_set_two[2]

    array[3][0][0] = temp_value_set_three[0]
    array[3][0][1] = temp_value_set_three[1]
    array[3][0][2] = temp_value_set_three[2]




def main():
    a = np.zeros((6,3,3))
    init_cube(a)

    #Right
    #rotate_up_right(a) 
    #rotate_up_right_prime(a)

    #Left
    #rotate_up_left(a)
    #up_left_prime(a)

    #Up
    #rotate_up(a)
    #rotate_up_left_prime(a)

    #Front
    #rotate_front(a)
    #rotate_prime_front(a)

    #Back
    #rotate_back(a)
    #rotate_back_prime(a)
    print(a)


if __name__ == '__main__':
    main()