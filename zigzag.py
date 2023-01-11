indent = 4
for i in range(4, 0, -1):
    print("  "*indent, end="")
    indent = indent-1
    print("****")
for i in range(0, 4):
    print(" "*indent, end="")
    indent = indent+1
    print("****")
