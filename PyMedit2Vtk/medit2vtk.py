import sys
import regex

def medit_format(in_file):
	try:
		m_version = 0
		m_dimension = 0

		medit_file = open(in_file)
		flag = True

		i=0
		while flag:
			i += 1
			line = medit_file.readline()
			if "MeshVersionFormatted" in line:
				m_version = int(line.split()[1])
			elif "Dimension" in line:
				m_dimension = int(line.split()[1])
			elif "Vertices" in line:
				flag = False
			elif len(line) == 0:
				raise Exception("EOF reached, Mesh File isn't well formatted")
			elif line.isspace():
				continue
			else:
				raise Exception("Mesh File isn't well formatted")

		m_vertices = int(medit_file.readline())

		vertices = list()

		for vertex in xrange(m_vertices):
			vertices.append(medit_file.readline)

		#flag = True
		m_objects = list()
		m_colors = set()


		while True:
			if m_dimension == 3:
				line = medit_file.readline()
				
				if "Tetrahedra" in line:
					break
				elif len(line) == 0:
					raise Exception("EOF reached, Mesh File isn't well formatted")

		while True:
			line = medit_file.readline()
			if len(line) == 0:
				break
			else:
				if m_dimension == 3:
					m_objects.append(line.split()[0:-2])
					m_colors.add(line.split()[-1])


		print m_colors

		medit_file.close()

		return (vertices,m_objects,m_colors)

	except Exception as e:
		print e


def create_vtk(vertices,objects,colors):
	pass

if __name__ == "__main__":
	if len(sys.argv) == 3:
		(vertices,objects,colors) = medit_format(sys.argv[1])
		create_vtk(vertices,objects,colors)
		print objects

	else:
		sys.stderr.write('the script needs only 2 arguments and you passed: %d\n' %(len(sys.argv)-1))