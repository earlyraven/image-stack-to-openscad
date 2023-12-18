import argparse

class Cube:
    def __init__(self, position, size, centered=False):
        self.position = position
        self.size = size
        self.centered = centered

    def scadify(self):
        output = "translate(" + str(self.position) + ") {"
        output += f"cube({self.size}"
        if self.centered:
            output += ", center=true"
        output += ");"
        output += "}\n"
        return output

class CubeGroup:
    def __init__(self, cubes, position=[0, 0, 0]):
        self.position = position
        self.cubes = cubes

    def scadify(self):
        output = "translate(" + str(self.position) + ") {\n"
        output += "group() {\n"
        item_list = ""
        for cube in self.cubes:
            item_list += cube.scadify()
        output += item_list
        output += "}\n"
        output += "}\n"
        return output

def load_file(file_path, position_index, voxel_size):
    cubes = []
    with open(file_path, 'r') as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char == '1':
                    cubes.append(Cube([voxel_size * x, voxel_size * y, position_index * voxel_size], size=voxel_size, centered=False))
    return cubes

def main():
    parser = argparse.ArgumentParser(description="Generate OpenSCAD code for cubes based on input files.")
    parser.add_argument("--with", nargs='+', dest="file_paths", required=True, help="List of file paths for input files.")
    parser.add_argument("--vs", type=int, default=4, help="Voxel size. Specify the size of each voxel (default is 4).")

    args = parser.parse_args()
    file_paths = args.file_paths
    voxel_size = args.vs

    cube_groups = []

    for idx, file_path in enumerate(file_paths):
        cubes = load_file(file_path, idx, voxel_size)
        cube_group = CubeGroup(cubes)
        cube_groups.append(cube_group)

    top_level_group = CubeGroup(cube_groups)

    print("// Top Level Cube Group")
    print(top_level_group.scadify())

if __name__ == "__main__":
    main()
