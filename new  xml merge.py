import xml.etree.ElementTree as ET
import glob

def merge_xml_files(input_folder, output_file):
    # Parse the first XML file to get the structure for metadata
    first_file = glob.glob(f"{input_folder}/*.xml")[0]
    tree = ET.parse(first_file)
    root = tree.getroot()
    
    # Create a new root element for the merged XML
    merged_root = ET.Element('annotations')
    # Add the version, meta, and job details from the first XML
    merged_root.append(root.find('version'))
    merged_root.append(root.find('meta'))

    # Find the <image> elements from all XML files and add them to the merged_root
    image_id = 0

    for file_path in glob.glob(f"{input_folder}/*.xml"):
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Iterate over <image> elements in each XML
        for image_elem in root.findall('image'):
            # Update the image id to be sequential
            image_elem.set('id', str(image_id))
            image_id += 1

            # Append the image element to the merged_root
            merged_root.append(image_elem)

    # Write the merged XML content to the output file
    merged_tree = ET.ElementTree(merged_root)
    merged_tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"Merged XML saved to {output_file}")

# Specify the input folder containing XML files and the desired output file
input_folder = "C:/Users/11883/Desktop/fmp combined/combined/"
output_file = 'C:/Users/11883/Desktop/fmp combined/merged_annotations.xml'

merge_xml_files(input_folder, output_file)
