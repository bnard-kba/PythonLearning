# Write your code here :-)
def collatz(num):
    if num % 2 == 0:
        print(num//2)
        return num//2
    elif num % 2 ==1:
        print(num*3+1)
        return (num*3+1)



try:
    print('Enter a number: ')
    prompt = int(input())
    while prompt !=1:

        prompt = collatz(prompt)
except ValueError:
    print('Enter an INTEGER')



