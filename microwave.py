nitems=int(input("Enter the number of items \n"))
timeforone=float(input("Enter the single item heating time \n"))
if nitems == 1:
    trequired=timeforone
    print("The recommended heating time is %.2f"%trequired)
elif nitems == 2:
    tr=timeforone+timeforone*50/100
    print("The recommended heating time is %.2f"%tr)
elif nitems == 3:
    tr=2*timeforone
    print("The recommended heating time is %.2f"%tr)
else:
    print("Number of items is more\n")
