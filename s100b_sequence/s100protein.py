gene = open("s100b_protienNucleotide.txt", "r")

a=0;
t=0;
c=0;
g=0;

gene.readline()
gene.readline()
for line in gene:
 line = line.lower()

for char in line:
          if char == "a":
                  a=a+1
          elif char == "t":
          	 t=t+1
          elif char =='g':
            g=g+1
          elif char =='c': 
            c=c+1 
          else: 
           print('no_files'); 
k = a+t/ a+t+c+g; 
b = c+g/a+t+c+g;

print('the name of the a+t': k); 
print('sum of c+g': b); 
          
         

   
