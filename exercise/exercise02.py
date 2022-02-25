# 1) function to return even numbers
def even_number(number):
    even_list = []
    for i in range(number+1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list


number = int(input("Enter a number until you want to get even numbers: "))
evens = even_number(number)
print(evens)

# 2) Reverse the list
print(evens[::-1])