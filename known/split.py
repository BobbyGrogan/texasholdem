with open('article.txt') as f:
    lines = f.readlines()

all = ''.join(lines)

new = all.split('.jpg" alt="')

next = []
for one in new:
	jah = one[:80]
	g = jah.split("/></td>\n<td>")
	gu = g[-1].split("</td>\n<td>")
	g.pop
	g.append(gu)
	next.append(g)

for x in next:
	print("['", x[0][:-2], "' , '", x[1][:9], "' , '", x[1][16:23], "'],")
