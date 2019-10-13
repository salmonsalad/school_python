s_list = []

while True :
    want = input("Enter what you want (type quit to exit) : ")
    if want == 'quit' :
        break
    
    s_list.append(want)
    s_list.sort()
    
    for i, value in enumerate(s_list) :
        print(i + 1, value)