# coding: utf-8
import  sys,shutil,os
import numpy as np

f1 = open(sys.argv[1]) 
f2 = open(sys.argv[2]) 
f =float
def get_coord_from_pdb(col=1): #PDBファイルから座標をとってくる関数 col=1 or 2
	File = open(sys.argv[col])
	coord = []
	for line in File:
		if line.startswith("ATOM") or line.startswith("HETATM"):
			coord.append([f(line[31:38]),f(line[39:46]),f(line[47:54])])
	File.close()
	return coord
#print get_coord_from_pdb(1) #座標とってこれるかのテスト
coord_A = get_coord_from_pdb(1)
coord_B = get_coord_from_pdb(2)


def center_of_mass(coord): #座標から重心を計算する
	#それぞれの座標の総和を計算
	x = sum([f(coord[i][0]) for i in range(len(coord))])
	y = sum([f(coord[i][1]) for i in range(len(coord))])
	z = sum([f(coord[i][2]) for i in range(len(coord))])
	#重心の座標を計算
	comx = x/len(coord)
	comy = y/len(coord)
	comz = z/len(coord)
	com = [comx,comy,comz]
	return com

com_A = center_of_mass(coord_A)
com_B = center_of_mass(coord_B)

"""重心の計算ができてるかのテスト"""
#coord_test = get_coord_from_pdb(1)
#print coord_test
#print center_of_mass(coord_test)
""""""

def trans(coord,com): # 重心を原点にする
	trans_coord = []
	for i in range(len(coord)):
		trans_coord.append([f(coord[i][0] - com[0]),f(coord[i][1])-com[1],f(coord[i][2])-com[2]])
	return trans_coord

trans_A = trans(coord_A,com_A)
trans_B = trans(coord_B,com_B)

def make_sym_matrix(coord1,coord2): #対称行列つくる
	mat1 = np.array(coord1) #coord1から行列をつくる。このときはまだ行ベクトル
	mat2 = np.array(coord2) 

	a = np.add(mat1,mat2) #二つの行列の和
	b = np.subtract(mat1,mat2) #二つの行列の差
	B11 = 0
	B12 = 0
	B13 = 0
	B14 = 0
	B22 = 0
	B23 = 0
	B24 = 0
	B33 = 0
	B34 = 0
	B44 = 0
	for i in range(len(coord1)):
		B11 +=  b[i][0] * b[i][0] + b[i][1] * b[i][1] + b[i][2] * b[i][2]
		B12 +=  a[i][2] * b[i][1] - b[i][2] * a[i][1]
		B13 += -a[i][2] * b[i][0] + a[i][0] * b[i][2]
		B14 +=  a[i][1] * b[i][0] - a[i][0] * b[i][1]
		B22 +=  b[i][0] * b[i][0] + a[i][1] * a[i][1] + a[i][2] * a[i][2]	
		B23 +=  b[i][0] * b[i][1] - a[i][0] * a[i][1]
		B24 +=  b[i][0] * b[i][2] - a[i][2] * a[i][0]
		B33 +=  a[i][0] * a[i][0] + b[i][1] * b[i][1] + a[i][2] * a[i][2]	
		B34 +=  b[i][1] * b[i][2] - a[i][1] * a[i][2]
		B44 +=  a[i][0] * a[i][0] + a[i][1] * a[i][1] + b[i][2] * b[i][2]	
	B21 = B12
	B31 = B13
	B41 = B14
	B32 = B23
	B42 = B24
	B43 = B34
	sym_matrix = np.array([[B11,B12,B13,B14],[B21,B22,B23,B24],[B31,B32,B33,B34],[B41,B42,B43,B44]],dtype=float)
	return sym_matrix/len(coord1) 

sym_matrix = make_sym_matrix(trans_A,trans_B)
#print sym_matrix
#対称行列の固有値と固有ベクトルを計算
la,v = np.linalg.eig(sym_matrix)
#print la
#print v
#最小固有値に対応する固有ベクトル
index = np.where(la==min(la))[0][0]
#qは固有ベクトルの成分
q0 = v[0][index]
q1 = v[1][index]
q2 = v[2][index]
q3 = v[3][index]
q11 = 2*q0*q0 + 2*q1*q1 - 1
q12 = 2*q1*q2 - 2*q0*q3
q13 = 2*q1*q3 + 2*q0*q2
q21 = 2*q1*q2 + 2*q0*q3
q22 = 2*q0*q0 + 2*q2*q2 - 1
q23 = 2*q2*q3 - 2*q0*q1
q31 = 2*q1*q3 - 2*q0*q2
q32 = 2*q2*q3 + 2*q0*q1
q33 = 2*q0*q0 + 2*q3*q3 - 1
rot = np.array([[q11,q12,q13],[q21,q22,q23],[q31,q32,q33]])
print 'rot', rot

coord_freeze = np.array(trans_A)
coord_rotation = np.array(trans_B).T #あとでもう一回転置
print '固定する方の原子座標'
print coord_freeze
print 'まわす前の原子座標'
print coord_rotation #まわす前
coord_rotated = np.dot(rot,coord_rotation).T
print "まわしたあとの原子座標"
print coord_rotated

msd = 0
for i in range(len(coord_freeze)):
	msd += np.dot((coord_freeze[i] - coord_rotated[i]),(coord_freeze[i] - coord_rotated[i]))
rmsd = np.sqrt(msd/len(coord_freeze))
print "RMSD"
print rmsd

list_rotated = coord_rotated.tolist()
list_freeze = coord_freeze.tolist()

#書き込むファイル
output = open('tmp.txt','w')


norot = []
rota = []
for i in range(len(list_freeze)):
    norot.append("%4s%2s%5d%1s%-4s%8s%6s%8.3f%8.3f%8.3f%22s%-2s\n" %("ATOM"," ",i+1," ","C","MOL F 1"," ",list_freeze[i][0],list_freeze[i][1],list_freeze[i][2]," ","C"))
    rota.append("%4s%2s%5d%1s%-4s%8s%6s%8.3f%8.3f%8.3f%22s%-2s\n" %("ATOM"," ",len(list_freeze)+i+1," ","C","MOL R 1"," ",list_rotated[i][0],list_rotated[i][1],list_rotated[i][2]," ","C"))

for i in range(len(list_freeze)):
    output.write(norot[i])
for i in range(len(list_freeze)):
    output.write(rota[i])

output.close()
shutil.copyfile("tmp.txt",(str(sys.argv[3])))
os.remove("./tmp.txt")


