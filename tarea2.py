import random
def search_forward(node,graph):
	if(node==1):
		return []
	result=[]
	
	temp=[]
	for i in graph.dict:
		if(node not in graph.dict[i]):
			continue
		else:
			temp.append(i)
			
	temp.sort()
	a=search_forward(temp[0],graph)
	a.append(temp[0])
	return a
	

			
class graph:
	def __init__(self,n_vertex):
		self.dict={}
		for i in range(1,n_vertex+1):
			self.dict[i]=[]
		
	def add_vertex(self,vertex):
		self.dict[vertex]=[]
	def add_edge(self,a,b):
		self.dict[a].append(b)
	#def get_edges():
	#	edges=[]
	#	for i in self.dict.keys():
	#		dest=self.dict.keys()[i]
	def contains_edge(self,a,b):
		r=False
		for i in self.dict:
			if(b not in self.dict[i]):
				continue
			else:
				if(a==i):
					r=True
				else:
					continue
		return r
	def exist_edge(self,a,b):
		if(a not in self.dict):
			return False
		else:
			if(b not in self.dict[a]):
				return False
			else:
				return True
				
	def delete_edge(self,a,b):
		for i in self.dict:
			if(i==a):
				if(b not in self.dict[a]):
					continue
				else:
					self.dict[a].pop()
	def return_out(self):
		lines=[]
		for i in self.dict:
			line=""
			for k in self.dict[i]:
				line+=str(k)
				line+=" "
			line+="\n"
			lines.append(line)
		return lines
			

f_in=open("input.txt",'r')
line=f_in.readline().rsplit()
t_edges=int(line[0])
n_vertex=t_edges+1
b_edges=int(line[1])
f_edges=int(line[2])
c_edges=int(line[3])
	
g=graph(n_vertex)

fc={"f":f_edges,"b":b_edges}

pass #agregar condiciones

if(c_edges>=1):
	branches=[]
	for i in range(0,c_edges+1):
		branches.append(i+2)
		g.add_edge(1,i+2)
		if(i>0):
			dest=random.choice(branches[:i])
			g.add_edge(i+2,dest)
			if(sum(fc.values())>0):
				last=i+2
				while(True):
					t=random.choice(fc.keys())
					fws=search_forward(last,g)
				
					if(t=='f'):
						if(len(fws)==1):
							continue
							
						s=random.choice(fws[:-1])
						edge=[s,last]
						pass
					else:
						s=random.choice(fws)
						edge=[last,s]
						break
				

				g.add_edge(edge[0],edge[1])					
				fc[t]-=1
				if(fc[t]==0):
					del fc[t]
			pass
	base=c_edges+3
	
else:	
	base=2
	

for i in range(base,n_vertex+1):
	random.seed(None)
	rand=random.choice(range(2,i))
	g.add_edge(rand,i)
counter=0
while(sum(fc.values())>0):
		
			last=random.choice(range(2,t_edges+2))
			t=random.choice(fc.keys())
			fws=search_forward(last,g)
			
			if(t=='f'):
				if(len(fws)==1):
					
					continue
				s=random.choice(fws[:-1])
				edge=[s,last]
				
				pass
			else:
				s=random.choice(fws)
				edge=[last,s]
			
			if(g.contains_edge(edge[0],edge[1])):
				continue
			g.add_edge(edge[0],edge[1])					
			fc[t]-=1
			if(fc[t]==0):
				del fc[t]
		
f_in.close()


f_out=open("output.txt","w+")
first_line=str(t_edges+1)+"\n"
f_out.write(first_line)
out=g.return_out()
for i in out:
	f_out.write(i)
f_out.close()


