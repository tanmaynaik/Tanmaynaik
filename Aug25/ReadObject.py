try:
    f=open("Test.txt",'r',encoding='utf-8')
    print(f.read())
except:
     print("operation not perform....")
finally:
    f=open("Test.txt",'r',encoding="utf-8")
    f.close()