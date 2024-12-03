# # import xml.etree.ElementTree as ET

# # # Parse the XML file
# # tree = ET.parse("C:/Users/11883/Desktop/fmp combined/xml/merged_output.xml")  # Replace 'your_file.xml' with the actual file name
# # root = tree.getroot()

# # # Create a list to store image information
# # image_list = []
# # image_id_list=[]

# # # Iterate over each image element
# # for image in root.findall('image'):
# #     image_id = image.get('id')
# #     image_name = image.get('name')
# #     image_list.append(image_name)
# #     image_id_list.append(image_id)
    
# #     image_id_list=image_id

# # # Print the list of images
# # print(len(image_list))
# # print(len(image_id_list))
# # #print(image_list)
# import xml.etree.ElementTree as ET
# count=0
# def coount_check(p):
    
# # Parse the XML file
#     tree = ET.parse(p)  # Update with the actual file path
#     root = tree.getroot()

#     # Create lists to store image information
#     image_list = []
#     image_id_list = []

#     # Iterate over each image element
#     for image in root.findall('image'):
#         image_id = image.get('id')
#         image_name = image.get('name')
#         image_list.append(image_name)  # Append image name to the list
#         image_id_list.append(image_id)  # Append image id to the list

#     # Print the number of images and IDs
#     print(f"Number of images: {len(image_list)}")
#     print(f"Number of image IDs: {len(image_id_list)}")

#     # Uncomment below to see the lists if needed
#     # print(image_list)
#     # print(image_id_list)
#     print(len(set(image_list)))
#     print(len(set(image_id_list)))
#     count= count+len(image_list)
    
    

# path="C:/Users/11883/Desktop/fmp combined/combined/"
# for i in range(1,71):
#     p=path+str(i)+".xml"
#     coount_check(p)
# print(count)


# import xml.etree.ElementTree as ET

# # Function to count the number of images in each XML file
# def count_check(p, count):
#     # Parse the XML file
#     tree = ET.parse(p)
#     root = tree.getroot()

#     # Create lists to store image information
#     image_list = []
#     image_id_list = []

#     # Iterate over each image element
#     for image in root.findall('image'):
#         image_id = image.get('id')
#         image_name = image.get('name')
#         image_list.append(image_name)  # Append image name to the list
#         image_id_list.append(image_id)  # Append image id to the list

#     # Print the number of images and IDs
#     print(f"Number of images in {p}: {len(image_list)}")
#     print(f"Number of unique image names in {p}: {len(set(image_list))}")
#     print(f"Number of unique image IDs in {p}: {len(set(image_id_list))}")

#     # Update the count with the number of images found
#     count += len(image_list)
    
#     return count

# # Path to the folder containing the XML files
# path = "C:/Users/11883/Desktop/fmp combined/combined/"

# # Initialize the count variable
# count = 0

# # Iterate over the range of XML files
# for i in range(1, 71):
#     p = path + str(i) + ".xml"
#     count = count_check(p, count)

# # Print the total count of images across all XML files
# print(f"Total count of images across all XML files: {count}")
import xml.etree.ElementTree as ET

# Function to count the number of images and <box> tags in each XML file
def count_check(p, image_count, box_count):
    # Parse the XML file
    tree = ET.parse(p)
    root = tree.getroot()

    # Create lists to store image information
    image_list = []

    # Iterate over each image element
    for image in root.findall('image'):
        image_id = image.get('id')
        image_name = image.get('name')
        image_list.append(image_name)  # Append image name to the list
        
        # Count the number of <box> tags within the current <image>
        box_count += len(image.findall('box'))

    # Update the image count with the number of images found
    image_count += len(image_list)

    # Print the number of images and <box> tags in this XML file
    print(f"Number of images in {p}: {len(image_list)}")
    print(f"Number of <box> tags in {p}: {len(image.findall('box'))}")

    return image_count, box_count

# Path to the folder containing the XML files
path = "C:/Users/11883.SBLKSL/Downloads/additional_37_frames/merged/"

# Initialize the count variables
image_count = 0
box_count = 0

# Iterate over the range of XML files
for i in range(1, 2):
    p = path + str(i) + ".xml"
    image_count, box_count = count_check(p, image_count, box_count)

# Print the total count of images and <box> tags across all XML files
print(f"Total count of images across all XML files: {image_count}")
print(f"Total count of <box> tags across all XML files: {box_count}")
