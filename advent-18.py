filepath = 'input.txt'

in_data = []
with open(filepath) as fp:
   line = fp.readline()
   while line:
       in_data.append(line.strip('\n'))
       line = fp.readline()
       
#Up down left right
dirs = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

def processInstr(instrs,start):
  cur = start
  corners = []
  conc_corners = 0
  conv_corners = 0
  prevDir = in_data[-1].split()[0]
  perimeter = 0
  for inst in instrs:
    corners.append(cur)
    inst_split = inst.split()
    curDir = inst_split[0]
    steps = int(inst_split[1])
    cur = (cur[0]+dirs[curDir][0]*steps,cur[1]+dirs[curDir][1]*steps)
    if (prevDir == 'U' and curDir == 'R') or (prevDir == 'L' and curDir == 'U') or (prevDir == 'D' and curDir == 'L') or (prevDir == 'R' and curDir == 'D'):
      conc_corners+=1
    elif (prevDir == 'U' and curDir == 'L') or (prevDir == 'L' and curDir == 'D') or (prevDir == 'D' and curDir == 'R') or (prevDir == 'R' and curDir == 'U'):
      conv_corners+=1
    prevDir = curDir
    perimeter+=steps
  return corners, conc_corners, conv_corners, perimeter

def Area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

#Part 1
cur = (0,0)
corners, conc_corners, conv_corners, perimeter = processInstr(in_data,cur)
total_a = Area(corners)
print(perimeter + (total_a - conc_corners/4 - conv_corners*3/4 - (perimeter-len(corners))/2))

#Part 2
dir_inst = ['R','D','L','U']
instrs = []
for i,ins in enumerate(in_data):
  hexinst = ins.split()[2].strip('(').strip(')')
  steps = str(int(hexinst[1:6],16))
  instrs.append(dir_inst[int(hexinst[-1])]+' '+steps)

corners, conc_corners, conv_corners, perimeter = processInstr(instrs,cur)
total_a = Area(corners)
print(perimeter + (total_a - conc_corners/4 - conv_corners*3/4 - (perimeter-len(corners))/2))