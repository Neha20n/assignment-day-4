#Assignment Day 4
#Q.1 Create a file and Write, Read, Append
abc = open("HeyWorld.txt","w")
abc.write("I Love Lets Upgarde")
abc.close()
abc = open("HeyWorld.txt","r")
content = print(abc.read())
abc.close()
abc = open("HeyWorld.txt","a")
abc.write(" \nI like to Do study with Lets Upgrade")
abc.close()
