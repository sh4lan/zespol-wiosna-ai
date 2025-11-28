import cv2
import numpy as np
import matplotlib.pyplot as plt

def normalize_image(image):
    print("Performing image normalization...")
    
    # Min-Max Scaling
    min_max = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    
    # Z-score Normalization
    z_score = np.zeros_like(image, dtype=np.float32)
    for i in range(3):  # for each channel
        channel = image[:,:,i]
        mean = np.mean(channel)
        std = np.std(channel)
        z_score[:,:,i] = (channel - mean) / (std + 1e-8)  # adding small value to avoid division by zero
    z_score = cv2.normalize(z_score, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    # Histogram Equalization
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist_eq = cv2.equalizeHist(gray)
    print("Normalization complete.")
    return min_max, z_score, hist_eq

# Example usage
image_path = 'example.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Failed to load image from {image_path}")
else:
    print(f"Successfully loaded image from {image_path}")
    
    min_max, z_score, hist_eq = normalize_image(image)
    
    # Display the results
    plt.figure(figsize=(20, 5))
    plt.subplot(141)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.axis('off')
    
    plt.subplot(142)
    plt.imshow(cv2.cvtColor(min_max, cv2.COLOR_BGR2RGB))
    plt.title('Min-Max Scaling')
    plt.axis('off')
    
    plt.subplot(143)
    plt.imshow(cv2.cvtColor(z_score, cv2.COLOR_BGR2RGB))
    plt.title('Z-score Normalization')
    plt.axis('off')
    
    plt.subplot(144)
    plt.imshow(hist_eq, cmap='gray')
    plt.title('Histogram Equalization')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

print("Script completed")

def augment_image(image):
    print("Performing image augmentation...")
    
    # Rotation
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
    rotated = cv2.warpAffine(image, M, (cols, rows))
    
    # Flipping
    flipped = cv2.flip(image, 1)  # 1 for horizontal flip
    
    # Brightness adjustment
    bright = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
    
    # Add noise
    noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
    noisy = cv2.add(image, noise)
    
    print("Augmentation complete.")
    return rotated, flipped, bright, noisy

# Example usage

if image is None:
    print(f"Failed to load image from {image_path}")
else:
    print(f"Successfully loaded image from {image_path}")
    
    rotated, flipped, bright, noisy = augment_image(image)
    
    # Display the results
    plt.figure(figsize=(20, 5))
    
    plt.subplot(151)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.axis('off')
    
    plt.subplot(152)
    plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
    plt.title('Rotated')
    plt.axis('off')
    
    plt.subplot(153)
    plt.imshow(cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB))
    plt.title('Flipped')
    plt.axis('off')
    
    plt.subplot(154)
    plt.imshow(cv2.cvtColor(bright, cv2.COLOR_BGR2RGB))
    plt.title('Brightness Adjusted')
    plt.axis('off')
    
    plt.subplot(155)
    plt.imshow(cv2.cvtColor(noisy, cv2.COLOR_BGR2RGB))
    plt.title('Noisy')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

print("Script completed")

def denoise_image(image):
    print("Performing image denoising...")
    
    gaussian = cv2.GaussianBlur(image, (5, 5), 0)
    median = cv2.medianBlur(image, 5)
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)
    
    print("Denoising complete.")
    return gaussian, median, bilateral

if image is None:
    print(f"Failed to load image from {image_path}")
else:
    print(f"Successfully loaded image from {image_path}")
    
    gaussian, median, bilateral = denoise_image(image)
    
    # Display the results
    plt.figure(figsize=(20, 5))
    
    plt.subplot(141)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original (Noisy)')
    plt.axis('off')
    
    plt.subplot(142)
    plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
    plt.title('Gaussian Blur')
    plt.axis('off')
    
    plt.subplot(143)
    plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB))
    plt.title('Median Blur')
    plt.axis('off')
    
    plt.subplot(144)
    plt.imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB))
    plt.title('Bilateral Filter')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

print("Script completed")

def binarize_image(image):
    print("Performing image binarization...")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Global thresholding (Otsu's method)
    _, global_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Adaptive thresholding
    adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                            cv2.THRESH_BINARY, 11, 2)
    
    print("Binarization complete.")
    return global_thresh, adaptive_thresh

if image is None:
    print(f"Failed to load image from {image_path}")
else:
    print(f"Successfully loaded image from {image_path}")
    
    global_thresh, adaptive_thresh = binarize_image(image)
    
    # Display the results
    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(global_thresh, cmap='gray')
    plt.title('Global Thresholding')
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(adaptive_thresh, cmap='gray')
    plt.title('Adaptive Thresholding')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

print("Script completed")
#def detect_edges(image):
#    print("Performing edge detection...")
#    
#    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    
#    # Sobel
#    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
#    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
#    sobel = np.sqrt(sobelx**2 + sobely**2)
#    sobel = np.uint8(sobel / sobel.max() * 255)
#    
#    # Canny
#    canny = cv2.Canny(gray, 100, 200)
#    
#    # Laplacian of Gaussian
#    blur = cv2.GaussianBlur(gray, (3, 3), 0)
#    log = cv2.Laplacian(blur, cv2.CV_64F)
#    log = np.uint8(np.absolute(log))
#    
#    print("Edge detection complete.")
#    return sobel, canny, log
#
#if image is None:
#    print(f"Failed to load image from {image_path}")
#else:
#    print(f"Successfully loaded image from {image_path}")
#    
#    sobel, canny, log = detect_edges(image)
#    
#    # Display the results
#    plt.figure(figsize=(20, 5))
#    
#    plt.subplot(141)
#    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#    plt.title('Original')
#    plt.axis('off')
#    
#    plt.subplot(142)
#    plt.imshow(sobel, cmap='gray')
#    plt.title('Sobel')
#    plt.axis('off')
#    
#    plt.subplot(143)
#    plt.imshow(canny, cmap='gray')
#    plt.title('Canny')
#    plt.axis('off')
#    
#    plt.subplot(144)
#    plt.imshow(log, cmap='gray')
#    plt.title('Laplacian of Gaussian')
#    plt.axis('off')
#    
#    plt.tight_layout()
#    plt.show()
#
#print("Script completed")
