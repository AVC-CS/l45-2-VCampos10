import random


def main():
    
 numbers = []
 total = 0
 for i in range(5):
       numbers.append(random.randint(0,100))
       print (numbers[i], end = ' ')
       total += numbers[i]
 print(total)
    
 print(f'The random values are {numbers}')
 print(f'The Total is {total}')

 return numbers, total


if __name__ == '__main__':
    main()
