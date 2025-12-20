#!/usr/bin/python

def fun1():
    print("I am in fun1")

def num_gen():
    for x in range(10):
        if x%3 == 0:
            print(x)
def main():
    fun1()
    num_gen()

if __name__ == '__main__':
    main()
