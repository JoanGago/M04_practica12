import xml.etree.ElementTree as ET

"""

Creem una funció que crea un arxiu .xml i el mostra per consola.
L'arxiu .xml consta de:
 - 1 root
 - 5 childs
  - 4 subchilds per cada child
 - Un atribut per cada child
 
"""
def arxiuXML():
    root = ET.Element("students")

    child1 = ET.SubElement(root, 'student')
    child1.set('Grupo', 'A')
    name1 = ET.SubElement(child1, 'name')
    name1.text = "Joan"
    surname1 = ET.SubElement(child1, 'surname')
    surname1.text = "Gago"
    email1 = ET.SubElement(child1, 'email')
    email1.text = "joangago@gmail.com"
    dni1 = ET.SubElement(child1, 'dni')
    dni1.text = "47992745w"

    child2 = ET.SubElement(root, 'student')
    child2.set('Grupo', 'A')
    name2 = ET.SubElement(child2, 'name')
    name2.text = "Aleix"
    surname2 = ET.SubElement(child2, 'surname')
    surname2.text = "Alvarex"
    email2 = ET.SubElement(child2, 'email')
    email2.text = "aalvarez@gmail.com"
    dni2 = ET.SubElement(child2, 'dni')
    dni2.text = "21756635f"

    child3 = ET.SubElement(root, 'student')
    child3.set('Grupo', 'B')
    name3 = ET.SubElement(child3, 'name')
    name3.text = "Pablo"
    surname3 = ET.SubElement(child3, 'surname')
    surname3.text = "Rosado"
    email3 = ET.SubElement(child3, 'email')
    email3.text = "prosado@gmail.com"
    dni3 = ET.SubElement(child3, 'dni')
    dni3.text = "47329282a"

    child4 = ET.SubElement(root, 'student')
    child4.set('Grupo', 'B')
    name4 = ET.SubElement(child4, 'name')
    name4.text = "Roger"
    surname4 = ET.SubElement(child4, 'surname')
    surname4.text = "Sobrino"
    email4 = ET.SubElement(child4, 'email')
    email4.text = "rsobrino@gmail.com"
    dni4 = ET.SubElement(child4, 'dni')
    dni4.text = "20384332s"

    child5 = ET.SubElement(root, 'student')
    child5.set('Grupo', 'A')
    name5 = ET.SubElement(child5, 'name')
    name5.text = "Edgar"
    surname5 = ET.SubElement(child5, 'surname')
    surname5.text = "Romero"
    email5 = ET.SubElement(child5, 'email')
    email5.text = "eromero@gmail.com"
    dni5 = ET.SubElement(child5, 'dni')
    dni5.text = "47922032g"

    tree = ET.ElementTree(root)
    tree.write("Alumnes.xml")

    ET.indent(root)
    ET.dump(root)
