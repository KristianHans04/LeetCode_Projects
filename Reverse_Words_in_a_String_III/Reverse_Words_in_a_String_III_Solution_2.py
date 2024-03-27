s = "Habari yako Mr Kristian"
break_down = s.split()          # Splits the string into words
broken_list = []
for i in range(len(break_down)):
        invert = break_down[i][::-1]#Prints the inverted string
        broken_list.append(invert)

b=" ".join(broken_list)

print(b)