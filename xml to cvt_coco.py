import xml.etree.ElementTree as ET
import json
import os

def xml_to_coco(xml_path, json_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Initialize the structure for the COCO JSON
    coco = {
        "licenses": [{"name": "", "id": 0, "url": ""}],
        "info": {
            "contributor": "",
            "date_created": "",
            "description": "",
            "url": "",
            "version": "",
            "year": ""
        },
        "categories": [],
        "images": [],
        "annotations": []
    }

    # Map labels to category IDs
    label_to_id = {}
    category_id = 1
    for label in root.findall(".//label"):
        label_name = label.find("name").text
        coco["categories"].append({
            "id": category_id,
            "name": label_name,
            "supercategory": ""
        })
        label_to_id[label_name] = category_id
        category_id += 1

    annotation_id = 1
    for image in root.findall(".//image"):
        image_id = int(image.attrib["id"])
        image_name = image.attrib["name"]
        width = int(image.attrib["width"])
        height = int(image.attrib["height"])

        # Add image info
        coco["images"].append({
            "id": image_id,
            "width": width,
            "height": height,
            "file_name": image_name,
            "license": 0,
            "flickr_url": "",
            "coco_url": "",
            "date_captured": 0
        })

        # Iterate over all boxes and polygons in the image
        for box in image.findall(".//box"):
            category_name = box.attrib["label"]
            category_id = label_to_id[category_name]
            xtl = float(box.attrib["xtl"])
            ytl = float(box.attrib["ytl"])
            xbr = float(box.attrib["xbr"])
            ybr = float(box.attrib["ybr"])
            width = xbr - xtl
            height = ybr - ytl
            area = width * height

            # Add box annotation
            coco["annotations"].append({
                "id": annotation_id,
                "image_id": image_id,
                "category_id": category_id,
                "segmentation": [],
                "area": area,
                "bbox": [xtl, ytl, width, height],
                "iscrowd": 0,
                "attributes": {
                    "occluded": box.attrib["occluded"] == "1",
                    "rotation": 0
                }
            })
            annotation_id += 1

        for polygon in image.findall(".//polygon"):
            category_name = polygon.attrib["label"]
            category_id = label_to_id[category_name]
            points = [
                float(coord)
                for point in polygon.attrib["points"].split(";")
                for coord in point.split(",")
            ]
            xs = points[::2]
            ys = points[1::2]
            xtl, ytl, xbr, ybr = min(xs), min(ys), max(xs), max(ys)
            width = xbr - xtl
            height = ybr - ytl
            area = 0.5 * abs(
                sum(xs[i] * ys[i + 1] - xs[i + 1] * ys[i] for i in range(len(xs) - 1))
                + (xs[-1] * ys[0] - xs[0] * ys[-1])
            )

            # Add polygon annotation
            coco["annotations"].append({
                "id": annotation_id,
                "image_id": image_id,
                "category_id": category_id,
                "segmentation": [points],
                "area": abs(area),
                "bbox": [xtl, ytl, width, height],
                "iscrowd": 0,
                "attributes": {
                    "occluded": polygon.attrib["occluded"] == "1"
                }
            })
            annotation_id += 1

    # Write the COCO JSON to file
    with open(json_path, "w") as json_file:
        json.dump(coco, json_file, indent=4)

# Example usage:
xml_path = 'C:/Users/11883/Downloads/latest_5011/1.xml'
json_path = 'C:/Users/11883/Downloads/latest_5011/1.json'
xml_to_coco(xml_path, json_path)
