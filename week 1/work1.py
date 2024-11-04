# Write a program to calculate the area and perimiter of a rectangle.
# Ask user to enter with and height of tthe rectangle

width = int(input('Enter recctangle width: '))
height = int(input('Enter rectangle height:'))
area = width*height
perimeter = 2 * (width+height)
print(f'rectangel ({width}, {height})')
print(f'Area: {area}')
print(f'perimeter: {perimeter}')