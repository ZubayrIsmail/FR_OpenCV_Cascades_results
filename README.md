# FR_OpenCV_Cascades_results
Producing accuracy results of face validation using OpenCv library

To Run this program 

  1) Add training images to "images" folder with naming convention that has a unique ID as the first character. example "1_Dwayne_Johnson"
  2) Add testing images to "testing" folder with each individual ina separate folder. Use same naming convention as stated above.
  3) Run "collect_training_data" collecting the data from each person individually by changing the file path in line 51 
  4) Run the classifier 
  5) Run frcacades.py 
  
  
Results should display in format 

Actual ID
Predicted ID
Confusion matrix
Accuracy Score

[1, 3, 1, 3, 3, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 3, 3, 5, 5, 5, 3, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 5, 5, 4, 5, 5, 5, 5, 4, 4, 5, 4, 4]
[5, 2, 2, 2, 2, 4, 1, 1, 4, 5, 5, 1, 1, 5, 1, 4, 3, 0, 0, 5, 2, 1, 1, 4, 1, 4, 4, 3, 3, 3, 5, 5, 1, 4, 4, 2, 2, 2, 1, 2, 4, 2, 1, 1, 5, 3, 3, 3, 3, 2]
[[0 0 0 0 0 0]
 [0 6 1 0 1 2]
 [0 2 0 3 3 2]
 [0 1 4 1 2 2]
 [0 0 4 3 3 0]
 [2 3 2 1 0 2]]
0.24
