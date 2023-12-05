
  # translate([0, 2, 1]) {
  #     cube(cube_size, false);
  # }
CUBE_SIZE = 4

class Cube:
  def __init__(self, position, size=CUBE_SIZE, centered="false"):
    self.position = position
    self.size = size
    self.centered = centered
    self.centered_string = ""
    if centered == "true":
      self.centered_string = f", {self.centered}"
  def scadify(self):
    output = "translate(" + str(self.position) + ") {"
    output += f"cube({self.size}{self.centered_string});"
    output += "}\n"
    return output

class CubeGroup:
  def __init__(self, cubes, position=[0,0,0]):
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


def main():
  cubes = []
  for x in range(8):
    for y in range(8):
      cubes.append(Cube([CUBE_SIZE*x,CUBE_SIZE*y,0]))
  theGroup = CubeGroup(cubes)
  print(theGroup.scadify())

if __name__ == "__main__":
  main()
