try:
    f=open("Test.txt",'w',encoding="utf-8")

    f.write("With Object method ")
except:
    print("operation not perform....")
finally:
     f=open("Test.txt",'w',encoding="utf-8")
     f.close()