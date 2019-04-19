# ROS
Learning attempt on Robot Operating System.

ROS NODES: Data/Information processing software units.Provides modularity in big projects.

ROS TOPICS: Entities that transport information between nodes.Topic is identified by name and type.

Information is organised as a data structure [strings,integers,floating point numbers]

Important building blocks of a ROS application:
                                                  
(1)Publisher Nodes:-A ROS node that generates information is called a publisher. A publisher sends information to nodes via topics.      With robotics often these publishers are connected with sensors like cameras, encoders etc..
If you use the rosnode info command you can see with which topics a node is connected and if these are outbound or inbound connections.           
(2)Subscriber Nodes:-A ROS node that receives information is called a subscriber. It's subscribed to information in a topic and uses      topic callback functions to process the received information.
With robotics, subscribers typically monitor system states such as triggering an alert when the robot reaches joint limits.

A subscriber callback function processes the data from a topic it subscribes to only when a new data is published.

ROS FILE SYSTEM:
ROS workspace-
ROS workspace (catkin workspace) consists of different subspaces. A workspace is a folder to organize ROS project files.                ROS uses catkin, which is a build tool to compile source files into binary files. Your code goes into the src workspace folder and  catkin manages the other ones. 
                
       
A catkin ROS workspace contains three main spaces:

    src space: contains source code, this will be your main work folder
    
    devel space: contains setup files for the project ROS environment
    
    build space: contains the compiled binary files
    
First, create a new folder for your workspace:
        
    $ mkdir -p new_ros_ws/src

You can use the ls command to verify the new folder that was created.

Next move to your newly created workspace using the command:
      
    cd new_ros_ws.

Thereafter, setup the correct ROS environment using the command: 

    source /opt/ros/kinetic/setup.bash. 
Finally, we initialize catkin:

    $ catkin init
    $ catkin build
