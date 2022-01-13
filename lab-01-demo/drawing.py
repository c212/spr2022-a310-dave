import turtle
def main():
    filename = input("Please enter drawing filename: ")
    timmy = turtle.Turtle()
    screen = timmy.getscreen()
    file = open(filename, "r")
    for line in file: 
        text = line.strip()
        commandList = text.split(",")
        command = commandList [0]
        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            timmy.width(width)
            timmy.pencolor(color)
            timmy.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            timmy.width(width)
            timmy.pencolor(color)
            timmy.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            timmy.fillcolor(color)
            timmy.begin_fill()
        elif command == "endfill":
            timmy.end_fill()
        elif command == "penup":
            timmy.penup()
        elif command == "pendown":
            timmy.pendown()
        else:
            print("Unknown command found in file:")
    file.close()
    timmy.ht()
    screen.exitonclick()
    print("Program Execution Completed.")
if __name__ == "__main__":
    main()
