import cv2
import os

# Input and output folders
input_folder=r'E:\Jobs\happymonk\task1\task1dataset\train'
output_folder = r'E:\Jobs\happymonk\task1\augmented_images'


rotation_angles = [90]  
brightness_factors = [1.0] 
blur_kernels = [(7, 7)]

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        image = cv2.imread(input_path)

        # Apply rotation
        for angle in rotation_angles:
            rotated_image = cv2.warpAffine(image, cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1), image.shape[1::-1])
            output_path = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}_rotated_{angle}.jpg')
            cv2.imwrite(output_path, rotated_image)

        # Apply horizontal
        horizontal_flip = cv2.flip(image, 1)
        vertical_flip = cv2.flip(image, 0)
        output_path = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}_horizontal_flip.jpg')
        cv2.imwrite(output_path, horizontal_flip)

        for factor in brightness_factors:
            adjusted_image = cv2.convertScaleAbs(image, alpha=factor, beta=0)
            output_path = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}_brightness_{factor}.jpg')
            cv2.imwrite(output_path, adjusted_image)

        # Apply Gaussian blur
        for kernel_size in blur_kernels:
            blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
            output_path = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}_blur_{kernel_size[0]}.jpg')
            cv2.imwrite(output_path, blurred_image)
