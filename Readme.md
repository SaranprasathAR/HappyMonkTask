**TASK1 :**

STEPS CARRIED OUT:
1. Data Collection: Collect a dataset of images that contains the target objects, in this case, people. Ensure that the dataset is diverse and representative of the real-world scenarios you want to detect.
2. Augmentation: Augmentation is the process of increasing the dataset size by making changes to the data already present. ---> Use augmentation.py file for augmenting
  
4. Annotation: Annotate the images in the dataset by drawing bounding boxes around the people in each image. This step creates ground truth data for training the model.
5. Data Preparation: Split the annotated dataset into training and testing sets. It is important to have a sufficient number of images in both sets for accurate evaluation of the model's performance.
6. Model Training: Use the YOLO v8 architecture to train the object detection model on your custom dataset. This involves feeding the training images and their corresponding annotations into the model, adjusting the model's parameters, and optimizing it to learn the features of the person objects.
7. Model Evaluation: Evaluate the trained model using the testing set of images. Measure performance metrics such as precision, recall, and mean average precision (mAP) to assess how well the model can detect people in unseen images.

**OUTPUT:**
![image](https://github.com/SaranprasathAR/HappyMonkTask-Submission/assets/91614660/0b6f7642-d02c-4ed8-bc4a-f3f211d341b2)

**TASK 2:**

STEPS CARRIED OUT:

1. Data collection --> Face expression recognition dataset - kaggle link- https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset

2. Structuring the data directory


   ![image](https://github.com/SaranprasathAR/HappyMonkTask-Submission/assets/91614660/58977249-7477-4431-8379-fd25614c410a)

3. Training the YOLOv8 model on the collected dataset for the classification task (Define the task as "Classify")
   

   ![image](https://github.com/SaranprasathAR/HappyMonkTask-Submission/assets/91614660/72b127c7-8963-4ba9-ab12-6759df6999eb)


4. Use the weight of the trained model and test on new data (Images/Videos)

    ![image](https://github.com/SaranprasathAR/HappyMonkTask-Submission/assets/91614660/71b8b512-2a33-4ea9-8b29-925250463e03)
   
    ![326](https://github.com/SaranprasathAR/HappyMonkTask-Submission/assets/91614660/ac864744-b95a-42a8-9997-d28ff6568f17)

    ![output_1](https://github.com/SaranprasathAR/HappyMonkTask-Submission/assets/91614660/63267c12-4e69-4a46-8dd5-b852848a5143)


**TASK 3**

ESRGAN : ESRGAN Performed better than SRGAN


Input

![baboon](https://github.com/SaranprasathAR/HappyMonkTask-Submission/assets/91614660/826e35e9-a7ff-4019-9067-aa0c5b010e6e) 

Output

![baboon_ESRGAN](https://github.com/SaranprasathAR/HappyMonkTask-Submission/assets/91614660/cf0e87d7-d9f2-474c-b8e8-02732ae2315f)


SRResNet

Ouput:

<img width="959" alt="result" src="https://github.com/SaranprasathAR/HappyMonkTask-Submission/assets/91614660/71322b01-999b-4893-b52d-9f7153cd7840">


