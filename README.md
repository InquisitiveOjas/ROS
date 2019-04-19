# ROS
Learning attempt on Robot Operating System.

ROS NODES: Data/Information processing software units.Provides modularity in big projects.

ROS TOPICS: Entities that transport information between nodes.Topic is identified by name and type.

Information is organised as a data structure [strings,integers,floating point numbers]

Important building blocks of a ROS application:-
                                                  
(1)Publisher Nodes:-A ROS node that generates information is called a publisher. A publisher sends information to nodes via topics. With robotics often these publishers are connected with sensors like cameras, encoders etc..
If you use the rosnode info command you can see with which topics a node is connected and if these are outbound or inbound connections.

(2)Subscriber Nodes:-A ROS node that receives information is called a subscriber. It's subscribed to information in a topic and uses topic callback functions to process the received information.
With robotics, subscribers typically monitor system states such as triggering an alert when the robot reaches joint limits.
