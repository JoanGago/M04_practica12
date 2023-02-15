import xml.etree.ElementTree as ET
#Crea una funcio que la retorna amb XML




#Crea una funció
def Axml():
    # Crea el element root
    tree = ET.Element("students")

    # Crea els sub elements
    a = ET.SubElement(tree, "student")
    a.set("Atribut", "14")
    name = ET.SubElement(a, "name")
    name.text = "Aleix"
    surname = ET.SubElement(a, "surname")
    surname.text = "Alvarez"
    email = ET.SubElement(a, "email")
    email.text = "aalvarez22@jaumebalmes.net"
    dni = ET.SubElement(a, "dni")
    dni.text = "21778592F"

    b = ET.SubElement(tree, "student")
    b.set("Atribut", "88")
    name = ET.SubElement(b, "name")
    name.text = "Joan"
    surname = ET.SubElement(b, "surname")
    surname.text = "Gago"
    email = ET.SubElement(b, "email")
    email.text = "jgago22@jaumebalmes.net"
    dni = ET.SubElement(b, "dni")
    dni.text = "23423534W"

    c = ET.SubElement(tree, "student")
    c.set("Atribut", "14")
    name = ET.SubElement(c, "name")
    name.text = "Pablo"
    surname = ET.SubElement(c, "surname")
    surname.text = "Rosado"
    email = ET.SubElement(c, "email")
    email.text = "prosado22@jaumebalmes.net"
    dni = ET.SubElement(c, "dni")
    dni.text = "2359779F"

    d = ET.SubElement(tree, "student")
    d.set("Atribut", "88")
    name = ET.SubElement(d, "name")
    name.text = "Aitana"
    surname = ET.SubElement(d, "surname")
    surname.text = "Lopez"
    email = ET.SubElement(d, "email")
    email.text = "alopez22@jaumebalmes.net"
    dni = ET.SubElement(d, "dni")
    dni.text = "3473850W"

    e = ET.SubElement(tree, "student")
    e.set("Atribut", "14")
    name = ET.SubElement(e, "name")
    name.text = "Marina"
    surname = ET.SubElement(e, "surname")
    surname.text = "Galindo"
    email = ET.SubElement(e, "email")
    email.text = "mgalindo22@jaumebalmes.net"
    dni = ET.SubElement(e, "dni")
    dni.text = "3845839T"

    # Guarda l'arxiu XML amb la funció ElementTree
    tree = ET.ElementTree(tree)
    tree.write("students.xml")

    ET.indent(tree)
    # Mostra per consola
    ET.dump(tree)

Axml()