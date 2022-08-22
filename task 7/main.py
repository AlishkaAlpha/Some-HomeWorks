"""  Task 1   """
# from audioop import reverse


# user_int = input("Enter a Sentence: ")
# res=''

# # h = "".join(chr(ord(l)+1)for l in a)


# for i in user_int:
#     char_ord = ord(i)
#     if 97<= char_ord <= 122:
#         res+=chr(char_ord+1) 
#     else:
#         res+=i
    
 
        

# print(res)

        

# print("".join(b))


"""  End of Task 1   """


"""  Task 2   """
# user_int = input("Enter a Sentence: ").lower()
# result=''


# alphabet = (list(map(chr, range(97, 123))))

# for i in user_int:

#     if 97<= ord(i) <= 122:
#         result+=str(alphabet.index(i)+1)+','
#     else:
#         result+=i
# print(result)



"""  End of Task 2   """


"""  Task 3   """



# ferma = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}


# ferma_wealth = 0

# half_list=len(ferma)//2
# big_bro = ferma[:half_list]

# big_bro_wealth = 0
# little_bro = ferma[half_list:]
# little_bro_wealth = 0
# for i in big_bro:
#     if i in qiymetler:
#         big_bro_wealth +=qiymetler[i]
# for i in little_bro:
#     if i in qiymetler:
#         little_bro_wealth +=qiymetler[i]

# if little_bro_wealth!=big_bro_wealth:
#             if little_bro_wealth>big_bro_wealth:
#                result = (little_bro_wealth - big_bro_wealth)//2
#                print(big_bro_wealth+result,little_bro_wealth-result)
#             elif little_bro_wealth<big_bro_wealth:
#                 result =  (big_bro_wealth - little_bro_wealth)//2
#                 print(little_bro_wealth+result,big_bro_wealth-result)




"""  End of Task 3   """

"""  Task 4   """


# animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
# farm = ['inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek']
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}


# animal_int = animal.lower()
# b = {i:farm.count(i) for i in qiymetler if i in farm}

# if animal_int in farm:
#     counted= farm.count(animal_int)
#     percentage = (counted * 100)//len(farm)
#     total =  counted*qiymetler[animal_int]


        

# text = f"""
# Axtarilan Heyvan: {animal}
# {'-'*10}
# Fermadaki {animal_int} sayi:  {counted}
# Diger heyvanlara olan faizi: {percentage}
# {animal_int} umumi qiymeti: {total} AZN
# """
# print(text)
"""  End of Task 4   """

"""  Task 5   """


# user_int = input("Enter a Sentence: ")
# res=[]
# for i in user_int:
#     binar = ord(i)         
#     binar_val = bin(binar)
#     res.append(binar_val[2:])


# print(" ".join(res))


"""  End of Task 5   """

"""  Task 6   """
user_int = input("Rgb Color: ")
b = user_int.find('(')
c =user_int[b:]
print(c)

result = '#%02x%02x%02x' % c

print(result)

"""  End of Task 6   """

"""  Task 7   """
"""  End of Task 7   """