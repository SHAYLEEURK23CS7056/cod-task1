source=open("a.txt","w")
source.write("hi how are you? hope you are fine?")
source=open("a.txt","r")
destination=open("b.txt","w")
for lines in source:
    words=lines.split()
wordsrev=words[::-1]
destination.write(str(wordsrev))
destination=open("b.txt","r")
print(destination.read())