#Imports libraries
import xml.etree.ElementTree as et
import xml.dom.minidom as xdm

#Program that asks a user to enter a country, its continent, and population
def main():
    file_name = "lisakilker_module6.xml"
    #Creates a root element called "Nation"
    root = et.Element("Nation")
    tree = et.ElementTree(root)
    
    #Loops through the user input until they select Q to quit
    while True:
        #Asks the user to input the name of the country or Q to quit
        input_country = input("Please give me the name of a country or type Q to quit: ")
        #If user enters Q, program quits and says "Goodbye!"
        if input_country.strip().upper() == "Q":
            print("Goodbye!")
            break
        
        #Asks the user for additional input for continent and population
        input_continent = input(f"What continent is {input_country} in? ")
        
        #Asks the user to enter population, and checks that it's a valid number and converts it to a float
        while True:
            input_population = input(f"What is the population of {input_country} (in millions)? ")
            try:
                input_population = float(input_population)
                break
            except ValueError:
                print("Please enter a valid number for the population.")

        #Writes the input from the user to an XML file
        tree.write(file_name)
        #Parses through the existing XML file
        tree = et.parse(file_name)
        #Gets the root element of the XML tree
        root = tree.getroot()
        #Subroot element 1
        country = et.SubElement(root, "Country")
        name = et.SubElement(country, "Name")
        name.text = input_country
        #Subroot element 2
        continent = et.SubElement(country, "Continent")
        continent.text = input_continent
        #Subroot element 3
        population = et.SubElement(country, "Population")
        population.text = f"{input_population}"

        #Writes the user input to the XML file
        tree.write(file_name)
        #Displays a message in the terminal that the data has been added to the file
        print(f"{input_country} was added to {file_name}")

        #Prettify the XML file
        rough_string = et.tostring(root, 'utf-8')
        reparsed = xdm.parseString(rough_string)
        pretty_xml_as_string = reparsed.toprettyxml(indent="    ")
        
        #Opens the XML file and writes the data in a string in a pretty way
        with open(file_name, 'w') as file:
            file.write(pretty_xml_as_string)

#Calls the main function
if __name__ == "__main__":
    main()