'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members

    This function should remove all rows from currentMem containing 'no'
    in the 'Active' column and appends them to exMem.
    '''


def cleanFiles(currentMem, exMem):

    with open(currentMem, "r+") as active_mem:
        with open(exMem, "a+") as inactive_mem:

            lines = active_mem.readlines()

            inactive = [member for member in lines if "no" in member]

            # Go to the beginning of the currentMem file
            active_mem.seek(0)
            if len(inactive) > 0:
                active_mem.truncate(0)

            # If a member is inactive, add them to exMem, otherwise write them into currentMem
            for line in lines:
                if line in inactive:
                    inactive_mem.write(line)
                else:
                    active_mem.write(line)


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'P:\Liad\Coursera\Python\Exercising\members.txt'
exReg = 'P:\Liad\Coursera\Python\Exercising\inactive.txt'
cleanFiles(memReg, exReg)

headers = "Membership No  Date Joined  Active  \n"

with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())

