import mmap
import numpy as np
from PIL import Image
import time
import sys

def main():
    # Read input
    if len(sys.argv) != 3:
        print("Usage: python3 detect.py image_file_path output_file_path")
        sys.exit()
    image_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    # Load image
    image = Image.open(image_file_path)
    image = np.array(image)

    # Load model
    model = torch.jit.load("model.pt")
    model.eval()

    # Run model
    start = time.time()
    with torch.no_grad():
        output = model(torch.tensor(image).unsqueeze(0))
        output = output.numpy()
        output = output[0][0]
    end = time.time()
    print("Elapsed time:", end - start)

    # Save output
    output = Image.fromarray(output)
    output
