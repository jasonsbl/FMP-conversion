import json

# Function to calculate/alter segmentation, area, and bbox from the original data
def calculate_new_values(segmentation, area, bbox):
    x1, y1, x2, y2 = bbox
    width = x2
    height = y2
    new_bbox = [x1,y1,width,height]
    new_area=width*height
    new_segmentation=[[x1,y1,x1+width,y1,x1+width,y1+height,x1,y1+height]]


    return new_segmentation, new_area, new_bbox

# Function to transform the datase
def transform_data(original_data):
    new_data = {
        "info": {},  # Can map or leave empty
        "licenses": [],  # Can map or leave empty
        "images": [],
        "annotations": [],
        "categories": [
                    {
            "id": 1,
            "name": "Illustration Region",
            "supercategory": ""
        },
        {
            "id": 2,
            "name": "Text Region",
            "supercategory": ""
        },
        {
            "id": 3,
            "name": "Text Header Region",
            "supercategory": ""
        },
        {
            "id": 4,
            "name": "Advert Region",
            "supercategory": ""
        },
        {
            "id": 5,
            "name": "Title Region",
            "supercategory": ""
        }
        ]
    }

    # Add all images
    for img in original_data["images"]:
        new_data["images"].append({
            "id": img["id"],
            "file_name": img["file_name"],
            "width": img["width"],
            "height": img["height"]
        })

    # Add all annotations with modified values
    for ann in original_data["annotations"]:
        segmentation = ann["segmentation"]
        area = ann["area"]
        bbox = ann["bbox"]

        # Calculate new values using the custom function
        new_segmentation, new_area, new_bbox = calculate_new_values(segmentation, area, bbox)

        # Append transformed annotations
        new_data["annotations"].append({
            "id": ann["id"],
            "image_id": ann["image_id"],
            "category_id": ann["category_id"],  # Same category mapping as original
            "segmentation": new_segmentation,
            "area": new_area,
            "bbox": new_bbox,
            "iscrowd": ann["iscrowd"]
        })

    return new_data

# Reading original large JSON file
with open('C:/Users/11883/Downloads/latest_5011/1.json', 'r') as f:
    original_data = json.load(f)

# Transform the data
transformed_data = transform_data(original_data)

# Saving the transformed data to a new JSON file
with open('C:/Users/11883/Downloads/latest_5011/fmp_coco.json', 'w') as f_out:
    json.dump(transformed_data, f_out, indent=4)

print("Transformation complete. Transformed data saved to 'transformed_output.json'.")
