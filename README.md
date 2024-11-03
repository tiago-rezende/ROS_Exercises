# ROS_Exercises

Name: Tiago LOPES REZENDE
Email: tiago.lopes@ensta-paris.fr

##Homework 1: main/src/homework1/

The homework implements communication between four different nodes. Node A sends a message to Node B, which complements the message and sends it to Node C. Node C does the same, forwarding the message to Node D, which ultimately sends the final message back to Node A.
The implementation of Node A is as follows:
The callback(data) function is defined to handle incoming messages. Whenever a message is received on the subscribed topic, it logs the content of the message. The message() function creates a publisher named message_A to send messages of type String. It initializes a node called messager_A and sets the publishing rate to 0.5 Hz. Inside a loop, it sends the message "Hello World," logging it each time. Notably, it also calls the listener() function, which initializes another node and subscribes to the message_D topic.
The listener() function initializes yet another node called node_A and subscribes to the message_D topic, invoking the callback() function when messages are received. The main execution block ensures that the message() function is called, capturing any ROS interruptions as exceptions.
The other nodes were implemented in the following way:
The callback(data) function processes incoming messages, logging the content of the original message. It then creates a new message that prefixes the original message with a greeting in a different language, preparing it for publication. A publisher for the topic is initialized, and the new message is logged and published.
The listener() function sets up a node, subscribing to the last topic. It employs rospy.spin() to keep the node active and process any incoming messages. The execution block at the end ensures that the listener() function is called, starting the listening process.

##Homework Facial Expression Recognition: main/Facial Expression Recognition/

This homework implements a KNN algorithm to classify different faces into classes representing different expressions. After loading the images and converting them to NumPy arrays, the dataset is created using scikit-learn's function train_test_split. The data is then reshaped into one-dimensional arrays to facilitate processing with PCA (Principal Component Analysis), which reduces their dimensionality while preserving important information. Next, the KNN model is created using scikit-learn. Different numbers of neighbors are tested (from one to ten), and the number of folds defined for cross-validation is set to 5. The best number of neighbors found is then used to predict the validation dataset, and the classification report and confusion matrix are displayed.

