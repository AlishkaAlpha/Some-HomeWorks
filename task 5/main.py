"""   Task 1   """
# a = [3, 12, 48, 7, 57, 41, 76, 62, 16, 48, 59, 53, 60, 79, 71, 81, 88, 26, 45, 72, 25, 65, 53, 88, 79, 34, 42, 40, 45, 92, 52, 85, 90, 16, 37, 50, 96, 67, 7, 59, 3, 41, 40, 58, 83, 16, 47, 23, 5, 22]


# # a = [i**2 for i in a if i % 6 ==0]
# a = [i for i in a if i % 6 ==0]
# print(a)

# for i in a:
#     print(pow(i,2),end=" ,")


"""   End of Task 1   """


"""   Task 2   """
# # a = [i for i in range(-100,100) if i % 7 == 0 if i % 3 == 0]
# a = [i*3 for i in range(-100,100) if i % 7 == 0  ]

# print(a)


"""   End of Task 2   """

"""   Task 3   """

data = (1, 2, 3, True, False, 3.3)

data_list = list(data)
data_list.append((1, 2))
data_list.insert(0,'asdf')
data = tuple(data_list)

print(data)

# data = ('asdf', 1, 2, 3, True, False, 3.3, (1, 2))

# data = input("bura nese yazin: ")



"""   End of Task 3   """



"""   Task 4   """

# direc = dir(str)

# a = [i for i in direc if not "__" in i]
# print(a)

"""   End of Task 4   """