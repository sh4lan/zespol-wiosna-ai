from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import cv2

# Create a new YOLO model from scratch
#model = YOLO("yolo11n.yaml")

def make_image(path):
	# Load a pretrained YOLO model (recommended for training)
	model = YOLO("hm6m2p.onnx")
	
	# Train the model using the 'coco8.yaml' dataset for 3 epochs
	#results = model.train(data="dataset.yaml", epochs=10)

# Export the model to ONNX format
#success = model.export(format="onnx")
	results = model.predict(path)
	image = cv2.imread(path)
	print()
	for idx, r in enumerate(results):
		annotator = Annotator(image)
	
		boxes = r.boxes
		for box in boxes:
			b = box.xyxy[0]
			c = box.cls
			annotator.box_label(b, model.names[int(c)])
		img = annotator.result()
		cv2.imwrite(f'temp.png', cv2.resize(img, (960, 540)))
	return len(results)
		
#cv2.destroyAllWindows()
		
	#print(w.boxes)
