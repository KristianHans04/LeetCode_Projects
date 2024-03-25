s = "Habari yako Mr Kristian"
break_down = s.split()          # Splits the string into words
print(break_down)
for i in range(len(break_down)):{
        print(break_down[i][::-1], " ", end='') #Prints the inverted string
}